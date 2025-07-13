# predict_weather.py
import joblib
import datetime


def predict_today() -> tuple[int, int, int]:
    today = datetime.datetime.now()
    X = [[today.month, today.day]]

    temp = joblib.load("model/temp_model.pkl").predict(X)[0]
    rain = joblib.load("model/rain_model.pkl").predict(X)[0]
    hum = joblib.load("model/hum_model.pkl").predict(X)[0]

    return round(temp, 1), round(rain, 1), round(hum, 1)
