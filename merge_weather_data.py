def merge_weather_data():
    import os
    import pandas as pd
    from functools import reduce

    # data 폴더 없으면 생성
    os.makedirs("data", exist_ok=True)

    # CSV 불러오기
    temp_df = pd.read_csv("data/해남기온.csv", encoding="cp949")
    rain_df = pd.read_csv("data/해남강수량.csv", encoding="cp949")
    hum_df = pd.read_csv("data/해남습도.csv", encoding="cp949")

    # 컬럼명 통일
    temp_df.columns = ["date", "temperature_2m_max"]
    rain_df.columns = ["date", "precipitation_sum"]
    hum_df.columns = ["date", "humidity"]

    dfs = [temp_df, rain_df, hum_df]

    for df in dfs:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")
        if df["date"].isnull().any():
            print("Warning: date 열에 변환 실패된 값 있음. 해당 행은 제거합니다.")
            df.dropna(subset=["date"], inplace=True)

    merged_df = reduce(
        lambda left, right: pd.merge(left, right, on="date", how="outer"), dfs
    )

    cols_to_fill = merged_df.columns.difference(["date"])
    merged_df[cols_to_fill] = merged_df[cols_to_fill].fillna(0)

    merged_df.sort_values("date", inplace=True)

    print(merged_df.head())

    # 파일로 저장
    merged_df.to_csv("data/weather.csv", index=False)
    print("weather.csv 파일이 data 폴더에 생성되었습니다.")


merge_weather_data()
