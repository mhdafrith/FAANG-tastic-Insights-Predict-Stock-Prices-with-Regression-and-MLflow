# FAANG-tastic Insights: Predict Stock Prices with Regression, MLflow, and Streamlit

## 📊 Project Overview

**FAANG-tastic Insights** is a machine learning project designed to predict stock prices of FAANG companies (Facebook, Amazon, Apple, Netflix, and Google) using regression models. The project integrates **MLflow** for tracking experiments and **Streamlit** for an interactive dashboard to visualize predictions.

## 🚀 Features

- Stock price prediction using **Linear Regression** and **Random Forest Regressor**
- Model evaluation with **R² Score**, **RMSE**, and **MAE**
- Experiment tracking and model management with **MLflow**
- Interactive web dashboard powered by **Streamlit** for dynamic visualization

## 📂 Project Structure

```
FAANG-tastic-Insights/
├── app.py                        # python_file web application for streamlit
├── faang_model_train.ipynb       # python_notebooks for EDA and model development
├── mlfow.db                      # mlflow metadata storage
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mhdafrith/FAANG-tastic-Insights-Predict-Stock-Prices-with-Regression-and-MLflow.git
   cd FAANG-tastic-Insights
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🧪 Running the Project

### 1. **Model Training with MLflow:**
```bash
mlflow run .
```
This will execute the experiment and log metrics, parameters, and artifacts.

### 2. **Launch the Streamlit App:**
```bash
streamlit run app.py
```
This opens an interactive dashboard in your browser for dynamic stock price predictions.

## 📈 Model Evaluation Metrics

- **R² Score:** Measures how well the model explains variance.
- **RMSE (Root Mean Square Error):** Indicates the model’s prediction error.
- **MAE (Mean Absolute Error):** Average absolute error between predicted and actual values.

## 🗃️ Technologies Used

- **Python**: Data processing and model development
- **Pandas, NumPy, Matplotlib, Seaborn**: Data analysis and visualization
- **Scikit-learn**: Machine learning models
- **MLflow**: Experiment tracking and model management
- **Streamlit**: Interactive web-based data visualization

## 📢 Acknowledgements
- **Guvi** for providing the data science learning platform and support.
- **FAANG companies** for inspiring the dataset and predictive analysis
- **MLflow & Streamlit communities** for powerful tools and resources

## 🤝 Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-xyz`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-xyz`)
5. Create a pull request

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

**Happy Predicting! 🚀**

