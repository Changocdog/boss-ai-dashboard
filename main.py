import streamlit as st
import pandas as pd
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def suggest_task():
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You're an assistant that helps automate video creation tasks."},
                {"role": "user", "content": "Give me one new automation task."}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {e}"

data = [
    {"timestamp": "2025-05-23 10:15", "task_type": "Script Writing", "status": "Completed"},
    {"timestamp": "2025-05-23 10:30", "task_type": "Video Editing", "status": "In Progress"},
    {"timestamp": "2025-05-23 10:45", "task_type": "Upload", "status": "Pending"}
]
df = pd.DataFrame(data)

st.set_page_config(page_title="Boss AI Dashboard", layout="wide")
st.title("Boss AI Monitoring Dashboard")

c1, c2, c3 = st.columns(3)
c1.metric("✅ Completed", len(df[df.status == "Completed"]))
c2.metric("⏳ In Progress", len(df[df.status == "In Progress"]))
c3.metric("🔲 Pending", len(df[df.status == "Pending"]))

st.write("### Task Log")
st.dataframe(df)

st.write("### 🤖 Generate Task")
if st.button("Suggest Task"):
    st.success(suggest_task())
