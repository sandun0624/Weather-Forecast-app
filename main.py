import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place:")
days = st.slider(label="Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox(label="Select data to view", options=("Temperature", "Sky"))

st.subheader(f"{option} for the Next {days} days in {place}")

dates = ["2024-08-26", "2024-08-27", "2024-08-28"]
temperatures = [10,11,15]

figure = px.line(x=dates, y=temperatures, labels={"x": "Dates", "y": "Temperature (C)"})
st.plotly_chart(figure)