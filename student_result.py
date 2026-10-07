import streamlit as st
import pickle
import pandas as pd

st.set_page_config(layout='centered', page_title="Student Result Prediction")
st.title("Student Result Prediction")

# Basic text
st.write("This app will predict the result of a student based on the number of hours they study and their previous exam score.")
st.write("first tried streamlit app")
st.subheader("Try your result too.")


# load model and preprocessing.
model = pickle.load(open("ML class/Student_result_prediction.pkl", "rb"))

# def clear_text():
#     st.session_state["num_hours"] = 0
#     st.session_state["prev_score"] = 0


with st.form(key="student_form"):
    num_hours = st.number_input("Enter the number of hours you study daily", min_value=0, max_value=24, value=0, step=1)
    prev_score = st.number_input("Enter your previous exam score", min_value=0, max_value=100, value=0, step=1)
    submit = st.form_submit_button(label="Submit", type='primary')
    # clear = st.form_submit_button("clear", on_click=clear_text)

if submit:
    new_data = pd.DataFrame({
    "Study Hours": [num_hours], 
    "Previous Exam Score": [prev_score]
    })
    pred  = model.predict(new_data)[0]

    if pred ==1:
        st.success("🎉 Result: Pass")
    else:
        st.error("❌ Result: Fail")

# if clear:
#     clear_text()
