# train_model.py
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
import os


def train_models(csv_path: str = "data/weather.csv"):
    df = pd.read_csv(csv_path)

    # 'humidity' 컬럼명에 맞게 결측치 제거
    df = df.dropna(
        subset=["date", "temperature_2m_max", "precipitation_sum", "humidity"]
    )

    # 날짜에서 월, 일 추출
    df["month"] = pd.to_datetime(df["date"]).dt.month
    df["day"] = pd.to_datetime(df["date"]).dt.day

    # 특징 변수
    X = df[["month", "day"]]

    # 타겟 변수
    y_temp = df["temperature_2m_max"]
    y_rain = df["precipitation_sum"]
    y_hum = df["humidity"]

    # 모델 선언
    temp_model = RandomForestRegressor(random_state=42)
    rain_model = RandomForestRegressor(random_state=42)
    hum_model = RandomForestRegressor(random_state=42)

    # 모델 학습
    temp_model.fit(X, y_temp)
    rain_model.fit(X, y_rain)
    hum_model.fit(X, y_hum)

    # 모델 저장용 폴더 생성
    os.makedirs("model", exist_ok=True)

    # 모델 저장
    _ = joblib.dump(temp_model, "model/temp_model.pkl")
    _ = joblib.dump(rain_model, "model/rain_model.pkl")
    _ = joblib.dump(hum_model, "model/hum_model.pkl")

    print("모델 학습 완료 및 저장됨.")


# 아래는 테스트용으로 직접 실행 시
if __name__ == "__main__":
    train_models()
