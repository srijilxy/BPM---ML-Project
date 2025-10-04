# BPM Prediction Web App (Beats Per Minuts)

A machine learning-powered web application for predicting the Beats Per Minute (BPM) of a music track using audio and track features. Built with Flask and scikit-learn, this project demonstrates end-to-end ML deployment for music analytics.

---

## Features

- **User-friendly web interface** for BPM prediction
- **Input form** for track features (e.g., Energy, RhythmScore, Loudness, etc.)
- **Automatic feature engineering** for advanced model accuracy
- **Real-time prediction** using a trained regression model
- **Modern, music-inspired UI** with responsive design

---

## How It Works

1. **User enters track features** (e.g., RhythmScore, Energy, AudioLoudness, etc.) in the web form.
2. **App applies feature engineering** to generate additional features required by the model.
3. **Model predicts BPM** and displays the result instantly.

---

## Input Features

- `RhythmScore`
- `Energy`
- `AudioLoudness`
- `TrackDurationMs`
- `AcousticQuality`
- `InstrumentalScore`
- `VocalContent`
- `LivePerformanceLikelihood`
- `MoodScore`

*All features are numeric. Example values are provided in the form.*

---

## Engineered Features

The backend automatically computes additional features such as:
- RhythmScore_Squared
- Energy_Squared
- Live_Energy
- Energy_Loudness_Ratio
- Audio_Intensity
- Rhythm_Loudness
- Duration_Minutes
- Performance_Character
- Log_Duration
- Rhythm_Duration_Density
- Vocal_Energy
- Acoustic_Instrumental_Ratio
- Duration_Energy_Ratio
- Rhythm_Energy
- Mood_Rhythm

---

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository**
    ```bash
    git clone https://github.com/yourusername/bpm-prediction-app.git
    cd bpm-prediction-app
    ```

2. **Create a virtual environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Place your trained model**
    - Copy `bpm_prediction_model.joblib` into the project root or `app` folder.

### Running the App

```bash
python run.py
```

Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

---

## Project Structure

```
BPM/
├── flask-model-app/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── templates/
│   │   │   └── index.html
│   ├── run.py
│   ├── requirements.txt
│   └── bpm_prediction_model.joblib
```

---

## Customization

- **Model:** Replace `bpm_prediction_model.joblib` with your own trained regression model.
- **Features:** Update `FEATURES` and `fe(df)` in `__init__.py` for new features.
- **UI:** Modify `index.html` and CSS for your branding.

---

## License

MIT License

---

## Credits

- [Flask](https://flask.palletsprojects.com/)
- [scikit-learn](https://scikit-learn.org/)
- [Bootstrap](https://getbootstrap.com/)

---

## Dataset
For dataset , visit : https://www.kaggle.com/competitions/playground-series-s5e9/data?select=train.csv

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## Author
Srijil Sunil
