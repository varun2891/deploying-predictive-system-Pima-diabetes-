# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 15:44:20 2024

@author: Hp
"""

import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('C:/Users\Hp\Downloads/machinelearning/trained_model.sav','rb'))

# Creating a function for prediction
def diabetes_prediction(input_data):
    

    # changing the input data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are finding the output for one instance
    reshaped_numpy_array = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_as_numpy_array)
    print(prediction)
    if (prediction[0]) == 0:
      return "The patient is non-diabetic"
    else:
      return 'The patient is diabetic'
  
    
  
  def main():
      
      # giving a title
      st.title("Diabetes Prediction Web App")
      
      # getting the input data from the user
      
      pregnancies = st.text_input("Number of pregnancies")
      glucose = st.text_input("glucose level")
      BloodPressure = st.text_input("Blood pressure level")
      SkinThickness = st.text_input("Skin Thickness")
      Insulin = st.text_input("Insulin Level")
      BMI = st.text_input("BMI level")
      DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function Level")
      Age = st.text_input("Age of the person")
      
      # code for prediction
      diagnosis = ''
      
      # creating a button for prediction
      if st.button("Diabetes test result"):
          diagnosis = diabetes_prediction([pregnancies, glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age ])
      
      if st.success(diagnosis):

if __name__ = "__main__":
    main()
    
     
      
      
  
 
  
    
  
    
  
    
  
    
  
    
  
    
  
    
  
    
  
    
  


