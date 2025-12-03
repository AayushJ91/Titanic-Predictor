# 🚢 Titanic Survivla Prediction App

## Introduction
This Streamlit application predicts the survival of a passenger based on their trip and demographical details. User can interactivvely create a passenger to test the prediction.


## Project Details

### *Model Performance & Selection*: 
The final model is **Gradient Boosting Classifier** which was selcted after evaluating several algorithms

### *Final Model Accuracy*:
 The model achieved an accuracy score of **82%** on the test dataset.

### *Data Preprocessing and Feature Engineering*:
Data Cleaning was performed by basic numpy and pandas operations, including **Handling Missing Values** and **One Hot Encoding** (for "Embarked" and "Sex").

### *Frontend and app*:
The frontend was made using **Streamlit** and is hosted live on Streamlit Community Cloud.


## 🔨 Technologies Used
* **Python 3.x**
* **Scikit-learn**: for model training and evaluation
* **Pandas / Numpy**: for data preprocessing
* **Streamlit**: for interface designing and app deployment
* **Pickle**: for saving and loading the model


## 💻 Local Setup Instructions

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/AayushJ91/Titanic-Predictor
    cd titanic-survival-prediction
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the App**
    ```bash
    streamlit run app.py
    ```