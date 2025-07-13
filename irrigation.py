# irrigation.py


def calculate_water_amount(temp: int, rain: int, hum: int, soil_moisture: float):
    base = 100

    if temp > 30:
        base += 50
    if rain > 1:
        base -= 40
    if hum > 80:
        base -= 20

    if soil_moisture > 70:
        base = 0
    elif soil_moisture < 30:
        base += 30

    return max(0, base)


def water_plant(amount: int):
    if amount > 0:
        print(f"[💧] 물 {amount}ml 주입 중...")
        # GPIO 사용 시: 모터 작동 코드 위치
    else:
        print("[✅] 토양이 충분히 촉촉하여 물 주기 생략.")
