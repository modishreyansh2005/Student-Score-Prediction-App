import streamlit as st
import pickle

st.title('Student Score Prediction App')
st.write('Enter study hours to predict student exam Score')
st.write("Note: Can'nt Enter The Value in More Than 8 Hours")


# Number Input
study_hours = st.number_input('Study Hours', min_value=0, max_value=24, step=1)

# Predict button
if st.button('Predict'):
    model = pickle.load(open('student_model.pkl', 'rb'))
    predition = model.predict([[study_hours]])
    st.wricte(f'Predicted Exam Score: {prediction[0]}')


