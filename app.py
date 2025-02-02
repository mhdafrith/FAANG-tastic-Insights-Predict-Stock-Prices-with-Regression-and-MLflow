import streamlit as st
import pickle
import numpy as np


page=st.sidebar.selectbox('Page Navigation', ["Prediction","About"])
st.sidebar.markdown("""-----""")
st.sidebar.write('Created by [Mohamed Afrith](https://www.linkedin.com/in/mohamed-afrit-s/)')
if page == 'Prediction':
    col1, col2, col3,col4,col5 = st.columns(5)

    # Display images in each column
    with col1:
        st.image('/Users/mohamedafrith/Downloads/meta_.png',width=100)

    with col2:
        st.image('/Users/mohamedafrith/Downloads/amazon_.jpg',width=100)

    with col3:
        st.image('/Users/mohamedafrith/Downloads/app_.jpg',width=100)
    
    with col4:
        st.image('/Users/mohamedafrith/Downloads/netflix-logo-icon.svg',width=90)
    
    with col5:
        st.image('/Users/mohamedafrith/Downloads/google_.png',width=100)

    
    
    
    # Set the title of the app
    st.title("FAANG Stock Price Prediction")

    # Load your trained model from the local pickle file
    try:
        with open('/Users/mohamedafrith/Downloads/model-2.pkl', 'rb') as file:
            model = pickle.load(file)
    except FileNotFoundError:
        st.error("The model file 'model-2.pkl' was not found in the specified directory. Please check the file path.")
        st.stop()

    # Create the user input section
    st.header("Enter the details to predict the Close price:")

    # Company selection (the display names will be mapped to numbers)
    company = st.selectbox("Select Company", ["Facebook", "Amazon", "Apple", "Netflix", "Google"])

    # Other numerical inputs
    open_price = st.number_input("Open", min_value=1.0, value=100.0, format="%.2f")
    year = st.number_input("Year", min_value=2000, max_value=2100, value=2025)
    month = st.number_input("Month", min_value=1, max_value=12, value=1)
    day = st.number_input("Day", min_value=1, max_value=31, value=1)

    # When the predict button is clicked
    if st.button("Predict Close Price"):
        # Map the company to its corresponding numeric value
        company_mapping = {
            "Facebook": 1,
            "Amazon": 2,
            "Apple": 3,
            "Netflix": 4,
            "Google": 5
        }
        company_encoded = company_mapping.get(company, -1)

        # Prepare the features array. Ensure the order matches the one used during model training.
        # In this example, the order is: [company, open_price, day, year, month]
        features = np.array([[company_encoded, open_price,  year, month,day]])
        
        try:
            # Make a prediction using the model
            prediction = model.predict(features)
            # Convert the predicted value to a float
            close_price = float(prediction[0])
            st.success(f"Predicted Close Price: {close_price:.2f}")
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")

if page=='About':

    st.title('FAANG-tastic Insights: Predict Stock Prices with Regression and MLflow')#project title
    st.header('Domain: Finance')
    st.header("Introduction:", divider='gray')#header
    st.markdown("FAANG-tastic Insights fuses regression analysis with MLflow to predict stock prices for the tech giants driving today's markets.Leverage historical data and cutting-edge machine learning to uncover trends and empower smarter investment strategies.")
    st.header('Approach:',divider="gray")
    st.markdown("***Data Collection & Preprocessing:***  Gather historical stock data for FAANG companies, clean and preprocess the dataset by handling missing values, normalizing features, and encoding categorical variables.")
    st.markdown("***Exploratory Data Analysis & Feature Engineering:*** Perform EDA to uncover trends, patterns, and correlations. Engineer relevant features—such as technical indicators or date-derived attributes—to boost model performance.")
    st.markdown("***Model Development & Experiment Tracking:*** Develop regression models to predict stock prices, evaluate their performance using appropriate metrics, and leverage MLflow to track experiments, manage models, and ensure reproducibility.")
    st.markdown("***Deployment & Monitoring:*** Deploy the best-performing model (e.g., via a Streamlit web application) for real-time predictions, and set up monitoring to continuously assess the model’s performance over time.")
    
    st.header("Skills Takeaway:",divider='gray')
    




    st.markdown("***Data Cleaning and Preprocessing:*** Learn how to gather, clean, and transform raw financial data for analysis and modeling.")#text content
    st.markdown("***Exploratory Data Analysis:*** Develop the ability to uncover patterns, trends, and correlations in stock market data through effective visualization and statistical analysis.")
    st.markdown("***Machine Learning Model Development:*** Master the process of developing robust regression models—from selecting the right algorithm and tuning hyperparameters to validating performance and ensuring generalization")
    
    st.markdown("***ML Flow:*** Use MLflow to log experiments, manage model versions, and ensure reproducibility throughout the machine learning lifecycle..")
    st.markdown("***Streamlit Application Development:*** Build interactive web applications with Streamlit to showcase your model's predictions and provide an intuitive user interface for stakeholders.")
    st.header("Result:" ,divider='gray')
    st.markdown("The FAANG-tastic Insights project successfully predicted stock prices using regression models, optimized with MLflow for experiment tracking. The model was deployed via a Streamlit app for real-time, interactive predictions.")
