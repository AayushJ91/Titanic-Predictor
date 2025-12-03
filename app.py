import streamlit as st
import pickle
import numpy as np

st.header("TITANIC Classifier")
st.write("Let's check whether the passenger you are making was dead or not")

def load_model():
    with open(r'Monthly\\Project\\best_model.pkl','rb') as file:
        model = pickle.load(file)
        return model
    
model = load_model()

pclass = st.number_input("The class in which your passenger travelled", max_value=3,min_value=1)
sex = st.radio("Gender of your passenger", ["Male", "Female"])
age = st.slider("Age of your passenger",0,100,50)
siblings = st.number_input("Number of siblings travelling along")
parents = st.number_input("Number of Children you are travelling with")
fare = st.number_input("Fare your passenger paid (in $)", max_value=512)
Embarked_Town = st.selectbox("Which town your passenger embarked at", ["Southampton", "Queenstown", "Cherboug"])



if sex == "Male":
    sex = 0
else:
    sex = 1

embarked_S = 0
embarked_Q = 0
if Embarked_Town == "Southampton":
    embarked_S = 1
elif Embarked_Town == "Queenstown":
    embarked_Q = 1

input = np.array([[pclass,sex,age,siblings,parents,fare,embarked_Q,embarked_S]])
if st.button("Dead or Survived"):
    output = model.predict(input)

    if (output):
        st.success("Alas! your passenger Died")
    else:
        st.success("Yeaah!! your passenger survived")