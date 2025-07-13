# app.py
import streamlit as st
import pandas as pd
import joblib
import datetime

# 모델 불러오기
temp_model = joblib.load('model/temp_model.pkl')
rain_model = joblib.load('model/rain_model.pkl')
hum_model = joblib.load('model/hum_model.pkl')

st.title("🌾 스마트팜 날씨 예측기")

# 날짜 선택
date = st.date_input("예측할 날짜를 선택하세요", datetime.date.today())

if st.button("예측 실행"):
    month = date.month
    day = date.day
    input_df = pd.DataFrame({'month': [month], 'day': [day]})

    temp_pred = temp_model.predict(input_df)[0]
    rain_pred = rain_model.predict(input_df)[0]
    hum_pred = hum_model.predict(input_df)[0]

    st.subheader("📈 예측 결과")
    st.metric("🌡 평균 기온 (°C)", f"{temp_pred:.1f}")
    st.metric("🌧 강수량 (mm)", f"{rain_pred:.1f}")
    st.metric("💧 습도 (%)", f"{hum_pred:.1f}")
