import pickle
import streamlit as st
from streamlit_option_menu import option_menu

heart_disease_model_lr = pickle.load(open('D:\hdp/heart_disease_model_lr.sav', 'rb'))

with st.sidebar:
    selected = option_menu('Heart Disease Prediction System', ['Heart Disease'], default_index=0)

if selected == 'Heart Disease':
    st.title('Heart Disease')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure ')

    with col2:
        chol = st.text_input('Serum ChoLestoraL in mg/dL ')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 129 mg/dl ')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic')

    with col2:
        thalach = st.text_input('maximum heart rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversible defect')

    diab_diagnosis = ''

    if st.button('Heart Disease Test Result'):
        try:
            # Convert input values to float
            age = float(age)
            sex = float(sex)
            cp = float(cp)
            trestbps = float(trestbps)
            chol = float(chol)
            fbs = float(fbs)
            restecg = float(restecg)
            thalach = float(thalach)
            exang = float(exang)
            oldpeak = float(oldpeak)
            slope = float(slope)
            ca = float(ca)
            thal = float(thal)

            # Make a prediction
            diab_prediction = heart_disease_model_lr.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

            if diab_prediction[0] == 1:
                diab_diagnosis = 'The Person is Diabetic'
            else:
                diab_diagnosis = 'The Person is Not Diabetic'
        except ValueError:
            diab_diagnosis = 'Please enter valid numeric values for the input features'

    st.success(diab_diagnosis)