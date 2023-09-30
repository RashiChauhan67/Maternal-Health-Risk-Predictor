import streamlit as st
import pickle

# import os

# file_path = os.path.abspath('/Users/HP/Documents/CODING/Jupyter/maternal_risk/model.pkl')

# with open(file_path, "rb") as pickle_in:
#     model = pickle.load(pickle_in)
# Load the model
pickle_in = open("model.pkl", "rb")
model = pickle.load(pickle_in)

if 'show_about_predictions' not in st.session_state:
    st.session_state.show_about_predictions = False

# Custom CSS style
st.markdown(
    """
    <style>
    .title {
        font-size: 36px;
        color: #FF6347;
        text-align: center;
        padding: 10px;
        margin-top: -60px;
    }
    .header {
        background-color: #FF6347;
        padding: 10px;
        margin-top: -10px;
        margin-bottom: 20px;
        border-radius: 10px;
    }
    .sidebar {
        background-color: #F0E68C;
        padding: 20px;
        border-radius: 10px;
    }
    .button {
        background-color: #FF6347;
        color: white;
        font-weight: bold;
        border-radius: 5px;
        padding: 5px 20px;
        text-align: center;
    }
    .button:hover {
        background-color: #FF4500;
    }
    .about-predictions {
        display: none;
        background-color: #F0F8FF;
        border-radius: 10px;
        padding: 20px;
        margin-top: 20px;
        text-align: center;
    }
    .image {
        width: 100%;
        border-radius: 10px;
        margin-top: 20px;
    }
    .footer-text {
        position: absolute;
        bottom: -40px;
        right: -10px;
        color: #FF6347;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def predict_model(age, sBP, dBP, bs, btemp, heart_rate):
    prediction = model.predict([[age, sBP, dBP, bs, btemp, heart_rate]])
    return prediction[0]

def main():
    st.markdown("<h1 class='title'>Maternal Health Risk Predictor</h1>", unsafe_allow_html=True)
    st.markdown("<div class='header'></div>", unsafe_allow_html=True)

    # Header and sidebar for user input
    # st.sidebar.header('User Input')
    age = st.slider("Age (in years)",0,100)
    sBP = st.text_input("Systolic BP (in mmHg)")
    dBP = st.text_input("Diastolic BP (in mmHg)")
    bs = st.text_input("Blood Sugar Level (in mmol/L.)",)
    btemp = st.text_input("Body Temp (in degrees Celsius)")
    heart_rate = st.slider("Heart Rate",50,100)

    result = ""
    if st.button("Predict", key="predict_button"):
        # if age.isdigit() and sBP.isdigit() and dBP.isdigit() and bs.isdigit() and btemp.isdigit() and heart_rate.isdigit():
            age = int(age)
            sBP = int(sBP)
            dBP = int(dBP)
            bs = int(bs)
            btemp = int(btemp)
            heart_rate = int(heart_rate)
            result = predict_model(age, sBP, dBP, bs, btemp, heart_rate)
        # else:
        #     st.sidebar.error("Please enter valid numeric values for input features.")
    
    if result:
        st.success(f"The predicted risk is: {result}")

    if st.button("Click to know about predictions"):
        if st.session_state.show_about_predictions:
            st.session_state.show_about_predictions = False
        else:
            st.session_state.show_about_predictions = True

    if st.session_state.show_about_predictions:
        st.markdown("<div class='about-predictions'>", unsafe_allow_html=True)
        st.markdown(
        "<span style='color: #e82525;'>Disclaimer: The model's training accuracy is 95%, but it may produce incorrect predictions during real-time use.</span>",
        unsafe_allow_html=True
        )
        st.write("Data has been collected from different hospitals, community clinics, maternal health cares through the IoT-based risk monitoring system.")
        st.write("Age: Age in years when a woman is pregnant.")
        st.write("Systolic BP: Upper value of Blood Pressure in mmHg, another significant attribute during pregnancy.")
        st.write("Diastolic BP: Lower value of Blood Pressure in mmHg, another significant attribute during pregnancy.")
        st.write("Blood Sugar Level (BS): Blood glucose levels are in terms of a molar concentration, mmol/L.")
        st.write("Body Temp: Body temperature in degrees Celsius.")
        st.write("Heart Rate: A normal resting heart rate in beats per minute.")
        st.write("Risk Level: Predicted Risk Intensity Level during pregnancy considering the previous attributes")
        st.write("Many pregnant women die from pregnancy issues due to a lack of information on maternal health care during and after pregnancy. This is more common in rural regions and among lower-middle-class families in emerging countries. Monitoring maternal health during pregnancy is essential for the proper growth of the baby and safe delivery.")
        st.image("maternal_health_image.jpg", use_column_width=True, caption="There is such a special sweetness in being able to participate in creation.")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        f"""
            <div class='footer-text'>
                <div class='bottom-right'>
                    Made by Rashi Chauhan &hearts;
                </div>
            </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == '__main__':
    main()



