from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load your trained pipeline
model = joblib.load('bpm_prediction_model.joblib')

# List all input feature names (except 'id' and 'BeatsPerMinute')
FEATURES = [
    'RhythmScore', 'Energy', 'AudioLoudness', 'TrackDurationMs', 'AcousticQuality',
    'InstrumentalScore', 'VocalContent', 'LivePerformanceLikelihood', 'MoodScore'
    # Add any other featuresthat model expects
]

# feature engineering function
def fe(df):
    # Example feature engineering (replace with your actual function)
    df['RhythmScore_Squared'] = df['RhythmScore'] ** 2
    df['Energy_Squared'] = df['Energy'] ** 2
    df['Live_Energy'] = df['LivePerformanceLikelihood'] * df['Energy']
    df['Energy_Loudness_Ratio'] = df['Energy'] / (df['AudioLoudness'] + 1e-6)
    df['Audio_Intensity'] = df['Energy'] * df['AudioLoudness']
    df['Rhythm_Loudness'] = df['RhythmScore'] * df['AudioLoudness']
    df['Duration_Minutes'] = df['TrackDurationMs'] / 60000
    df['Performance_Character'] = df['LivePerformanceLikelihood'] * df['MoodScore']
    df['Log_Duration'] = np.log1p(df['TrackDurationMs'])
    df['Rhythm_Duration_Density'] = df['RhythmScore'] / (df['TrackDurationMs'] + 1e-6)
    df['Vocal_Energy'] = df['VocalContent'] * df['Energy']
    df['Acoustic_Instrumental_Ratio'] = df['AcousticQuality'] / (df['InstrumentalScore'] + 1e-6)
    df['Duration_Energy_Ratio'] = df['TrackDurationMs'] / (df['Energy'] + 1e-6)
    df['Rhythm_Energy'] = df['RhythmScore'] * df['Energy']
    df['Mood_Rhythm'] = df['MoodScore'] * df['RhythmScore']
    return df


@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        # Get form data
        input_data = [float(request.form[feature]) for feature in FEATURES]
        # Create DataFrame for model
        df = pd.DataFrame([input_data], columns=FEATURES)
        # Apply your feature engineering function here if needed
        # For example: df = fe(df)
        # Predict
        df = fe(df)  # This adds engineered features
        prediction = model.predict(df)[0]
    return render_template('index.html', features=FEATURES, prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)