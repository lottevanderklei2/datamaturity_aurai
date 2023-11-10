# app.py

import streamlit as st
import pandas as pd
import plotly.express as px

# Sample data (replace this with your data)
data = {
    'Question': ['Business & Data Alignment', 
                 'Data Driven Organisation', 
                 'Data Governance & Management', 
                 'Data Architecture & Infrastructure', 
                 'Cloud', 
                 'ETL Processes', 
                 'Machine Learning engineering', 
                 'Innovation & Experimentation', 
                 'Data Analytics'],
}

df_questions = pd.DataFrame(data)

# Streamlit app
st.title("Data maturityscan Aurai")

# Initialize answers dictionary
answers = {}

# # Loop through each question
# for index, row in df_questions.iterrows():
#     st.write(f"### Question {index + 1}: {row['Question']}")
    
#     # Use unique key for each question's response input
#     response_key = f"response_{index}"
#     response = st.slider("Select your answer", min_value=1, max_value=5, key=response_key)
    
#     # Save the response in the answers dictionary
#     answers[row['Question']] = response

# # Display the answers
# st.write("### Your Answers:")
# print("Answers dictionary:", answers)
# answers_df = pd.concat([pd.DataFrame(answer, index=[0]) for answer in answers], ignore_index=True)
# # answers_df = pd.DataFrame(list(answers.items()), columns=['Question', 'Answer'])



# st.write(answers_df)

# # Create a radar chart based on the answers
# fig = px.line_polar(answers_df, r='Answer', theta='Question', line_close=True)
# st.write("### Radar Chart:")
# st.plotly_chart(fig)

# # Initialize answers list
# answers = []
# answers_df = pd.DataFrame(columns=['Question', 'Answer'])
# # Loop through each question
# for index, row in df_questions.iterrows():
#     st.write(f"### Question {index + 1}: {row['Question']}")
    
#     # Use unique key for each question's response input
#     response_key = f"response_{index}"
#     response = st.slider("Select your answer", min_value=1, max_value=5, key=response_key)
    
#     # Save the response in the answers list
#     answers.append({'Question': row['Question'], 'Answer': response})

# # Display the answers
# st.write("### Your Answers:")
# print("Answers list:", answers)

# # Create a DataFrame from the list of dictionaries
# answers_df = pd.DataFrame(answers)

# # Create a radar chart based on the answers
# fig = px.line_polar(answers_df, r='Answer', theta='Question', line_close=True)
# st.write("### Radar Chart:")
# st.plotly_chart(fig)

# Initialize an empty DataFrame with columns 'Question' and 'Answer'
answers_df = pd.DataFrame(columns=['Question', 'Answer'])

# Loop through each question
for index, row in df_questions.iterrows():
    st.write(f"### Question {index + 1}: {row['Question']}")
    
    # Use unique key for each question's response input
    response_key = f"response_{index}"
    response = st.slider("Select your answer", min_value=1, max_value=5, key=response_key)
    
    # Append the response as a dictionary to the answers_df DataFrame
    answers_df = pd.concat([answers_df, pd.DataFrame({'Question': [row['Question']], 'Answer': [response]})], ignore_index=True)

# Display the answers
st.write("### Your Answers:")
st.write(answers_df)

# Create a radar chart based on the answers_df DataFrame
fig = px.line_polar(answers_df, r='Answer', theta='Question', line_close=True)
st.write("### Radar Chart:")
st.plotly_chart(fig)


