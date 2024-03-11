import streamlit as st
import joblib

# Load pretrained model using joblib
regressor = joblib.load('regressor.pkl')

# Function to create predictor
def predict_Bike_Demand(Hour, Temperature, Wind_Speed, Visibility, Rainfall, Snowfall, Holiday, Functioning_Day, Month, Day):
    # Preprocess data
    # Convert hour to integer
    Hour = int(Hour)
    # Convert holiday to 0 or 1
    Holiday = 0 if Holiday == 'Yes' else 1
    # Convert functioning_day to 0 or 1
    Functioning_Day = 0 if Functioning_Day == 'Yes' else 1

    # Predict using the model
    prediction = regressor.predict([[Hour, Temperature, Wind_Speed, Visibility, Rainfall, Snowfall, Holiday, Functioning_Day, Month, Day]])
    
    if prediction < 0:
        return "Please enter valid details"
    else:
        prediction=int(prediction)
        return f"Number of bikes required for the mentioned date will be {prediction}"
    

# Streamlit code
st.set_page_config(page_title='Bike Demand Predictor', page_icon="🚲")

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: black;
        color: white;
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Streamlit code
st.title('Bike Demand Predictor')

Hour = st.selectbox('Hour', list(range(24)), index=0)
Temperature = st.number_input('Temperature', min_value=-100.0, max_value=100.0, value=0.0, step=0.1)
Wind_Speed = st.number_input('Wind Speed', min_value=0.0, max_value=10.0, value=0.0, step=0.1)
Visibility = st.number_input('Visibility', min_value=0.0, max_value=3000.0, value=0.0, step=1.0)
Rainfall = st.number_input('Rainfall', min_value=0.0, max_value=100.0, value=0.0, step=0.1)
Snowfall = st.number_input('Snowfall', min_value=0.0, max_value=10.0, value=0.0, step=0.1)
Holiday = st.radio('Holiday', ('Yes', 'No'))
Functioning_Day = st.radio('Functioning Day', ('Yes', 'No'))
Month = st.selectbox('Month', list(range(1,12)), index=0)
# Month = st.number_input('Month', min_value=1, max_value=12, value=1, step=1)
Day = st.selectbox('Day', list(range(1,31)), index=0)

if st.button('Predict'):
    result = predict_Bike_Demand(Hour, Temperature, Wind_Speed, Visibility, Rainfall, Snowfall, Holiday, Functioning_Day, Month, Day)
    st.write(result)





