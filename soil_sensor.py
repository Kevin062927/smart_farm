import random


def get_soil_moisture():
    """
    토양 수분 센서에서 데이터를 읽어오는 함수.
    현재 센서에서 데이터를 읽어올 수 없어 랜덤 값으로 대체.
    """
    # 0~100 사이의 랜덤 수분 값 (단위: %)
    moisture_value = random.uniform(0, 100)
    return round(moisture_value, 2)
