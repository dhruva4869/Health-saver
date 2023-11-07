import pickle
import streamlit as st
from streamlit_option_menu import option_menu
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))



with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Home','Diabetes Prediction',
                           'Heart Disease Prediction', 
                           'Graphs', 'Help'],
                          icons=['heart','activity','heart', 'activity', 'heart'],
                          default_index=0)
if selected == "Home":
    st.title("HEALTH SAVER")
    st.write("""
        The "Health Saver Web application" is a groundbreaking healthcare tool that predicts the likelihood of diseases 
             like Parkinson's and diabetes, enabling users to take proactive measures for better health. 
             Additionally, it provides valuable insights into the trends and patterns of these diseases over the years, 
             fostering awareness and informed decision-making for individuals and communities alike.
        By leveraging advanced technology and analyzing personal health data, genetic information, and 
             medical history, the Health Saver web application empowers users to make informed choices for disease 
             prevention and management.
    """)
    st.write("\n")
    st.write("\n")
    st.image('het.jpg', use_column_width=True, caption="Save your health with our App")


if (selected == 'Diabetes Prediction'):
    st.title('Diabetes Prediction using ML')
    col1, col2 = st.columns(2)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level (Plasma glucose concentration a 2 hours in an oral glucose tolerance test)')
    with col1:
        BloodPressure = st.text_input('Blood Pressure value (Diastolic blood pressure (mm Hg))')
    with col2:
        SkinThickness = st.text_input('Skin Thickness value (Triceps skin fold thickness (mm))')
    with col1:
        Insulin = st.text_input('Insulin Level (2-Hour serum insulin (mu U/ml))')
    with col2:
        BMI = st.text_input('BMI value')
    with col1:
        Age = st.text_input('Age of the Person')
    
    diab_diagnosis = ''
        
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, "0.5", Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    if diab_diagnosis: st.success(diab_diagnosis) 
    else: st.error(diab_diagnosis)

if (selected == 'Heart Disease Prediction'):
    st.title('Heart Disease Prediction using ML')
    
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex (1-Male, 0-Female)')
        
    with col1:
        cp = st.text_input('Chest Pain (Category 0, 1, 2, 3 types)')
        
    with col2:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col1:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (1 if yes else 0)')
        
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
        
    with col1:
        thal = st.text_input('inherited blood disorder?: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    # cholestrol = 250 resting electrocardio = 1 and exang (exercise induced angina) = 1
    # 1.8 row 15 for oldpeak = ST depression induced by exercise
    # slope of the peak exercise ST segment is 1
    # Major vessels colored by flourosopy = 0
    if st.button('Heart Disease Test Result'):
    # Convert text inputs to numeric values
        age_numeric = float(age)
        sex_numeric = int(sex)
        cp_numeric = int(cp)
        trestbps_numeric = float(trestbps)
        fbs_numeric = int(fbs)
        thalach_numeric = float(thalach)
        thal_numeric = int(thal)

        heart_prediction = heart_disease_model.predict([[age_numeric, sex_numeric, cp_numeric, trestbps_numeric, 250, fbs_numeric, 1, thalach_numeric, 1, 1.8, 1, 0, thal_numeric]])

        if (heart_prediction[0] == 1):
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    if heart_diagnosis: st.success(heart_diagnosis) 
    else: st.error(heart_diagnosis)


if selected == "Graphs":
    st.title("Informative Graphs we designed from our Models")
    st.subheader("Heart Disease Predictor graphs")
    st.write("Confusion Matrix")
    st.image("heart_conf_logistic_regr.png", use_column_width=100)
    st.write("ROC curve")
    st.image("heart_roc_logistic_regr.png", use_column_width=100)

    st.subheader("Diabetes Predictor graphs")
    st.write("Confusion Matrix")
    st.image("conf_diabetes_svm.png", use_column_width=100)
    st.write("ROC curve")
    st.image("roc_diabetes_svm.png", use_column_width=100)


if selected == "Help":

    st.title("Precautions for Individuals Managing Diabetes and Heart Disease\n\n")
    st.subheader("Introduction: ")
    st.write("\n")
    st.write("""Managing both diabetes and heart disease presents unique challenges. This article provides essential 
             precautions to navigate the 
             complexities of living with these conditions simultaneously, enhancing overall well-being and reducing 
             health risks.""")
    

    
    st.subheader("Precautions for Managing Diabetes:\n")
    st.image("dia.webp", width=900)
    st.write("""
        Regular Blood Sugar Monitoring: Individuals with Type 1 diabetes should monitor their blood sugar levels regularly, as prescribed by their healthcare provider. This helps in understanding and managing fluctuations in blood glucose levels.

        Insulin Management: Proper insulin management is crucial. Follow your prescribed insulin regimen, which may include multiple daily injections or an insulin pump.

        Dietary Control: Pay close attention to your diet. Focus on consistent carbohydrate intake, a balanced diet, and portion control. Consult a registered dietitian to create a personalized meal plan.

        Exercise Safely: Engage in regular physical activity but consult with your healthcare team to create an exercise plan that takes diabetes into account. Monitor blood sugar levels before and after exercise.

        Emergency Supplies: Always carry necessary supplies, such as glucose tablets or a glucagon kit, to address low blood sugar (hypoglycemia) emergencies.
        """)
    

    st.subheader("Precautions for Managing Heart Disease:\n")
    st.image("2.jpg", width=900)
    st.write("""
                Medication Compliance: Take prescribed heart medications regularly and as directed by your cardiologist. This may include medications for hypertension, high cholesterol, and blood thinners.

                Heart-Healthy Diet: Adopt a diet low in saturated and trans fats, sodium, and processed foods. Emphasize fruits, vegetables, whole grains, lean proteins, and healthy fats.

                Regular Exercise: Engage in regular physical activity to strengthen your heart and improve overall cardiovascular health. Consult your cardiologist to determine a suitable exercise regimen.

                Monitor Blood Pressure: Regularly check and manage your blood pressure. Your healthcare team may recommend home monitoring to track your readings between doctor's appointments.

                Stress Reduction: Practice stress management techniques, such as deep breathing exercises, meditation, or yoga, to reduce stress, which can impact heart health.

        """)
