# app.py

import streamlit as st
import pandas as pd
import plotly.express as px

# Sample data (replace this with your data)
data = {
    'Question': ['Q1', 'Q2', 'Q3', 'Q4', 'Q5'],
    'Answer1': [3, 4, 2, 5, 1],
    'Answer2': [2, 5, 3, 4, 1],
    'Answer3': [5, 1, 4, 2, 3],
}

df = pd.DataFrame(data)

# Streamlit app
st.title("Radar Chart App")

# Display the questions and answers
st.write("### Questions and Answers:")
st.write(df)

# Create a radar chart
fig = px.line_polar(df, r=df.iloc[:, 1:], theta='Question', line_close=True)
st.write("### Radar Chart:")
st.plotly_chart(fig)

