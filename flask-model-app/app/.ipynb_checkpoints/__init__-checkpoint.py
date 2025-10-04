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
    # Add any other features your model expects
]

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
        prediction = model.predict(df)[0]
    return render_template('index.html', features=FEATURES, prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)