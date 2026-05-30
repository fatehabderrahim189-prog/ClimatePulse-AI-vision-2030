import streamlit as st

st.set_page_config(page_title="ClimatePulse AI", layout="wide")

st.title("🌍 ClimatePulse AI")

st.write("AI system for climate impact analysis on productivity.")

temp = st.slider("Temperature", 20, 55, 35)
humidity = st.slider("Humidity", 10, 100, 50)

if st.button("Run Analysis"):
    score = 100 - (temp * 1.5) + (humidity * 0.3)

    st.metric("Productivity Score", round(score, 2))

    if score < 60:
        st.error("High Risk Climate Impact")
    else:
        st.success("Low Risk Climate Conditions")