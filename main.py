# main.py
from train_model import train_models
from predict_weather import predict_today
from soil_sensor import get_soil_moisture
from irrigation import calculate_water_amount, water_plant


def main():
    print("📊 모델 학습 중...")
    train_models()

    print("🌤️ 오늘 날씨 예측 중...")
    temp, rain, hum = predict_today()
    print(f"예측 → 기온: {temp}℃, 강수량: {rain}mm, 습도: {hum}%")

    soil = get_soil_moisture()
    print(f"🌱 현재 토양 습도: {soil}%")

    amount = calculate_water_amount(temp, rain, hum, soil)
    water_plant(amount)


if __name__ == "__main__":
    main()
