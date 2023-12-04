import pandas as pd
import numpy as np 
from joblib import load
from sklearn.model_selection import GridSearchCV
from xgboost import XGBClassifier

model = load('h1')

def predict_stroke_result(gender, age, hypertension, heart_disease, ever_married, avg_glucose_level, bmi, smoking_status):
    
    prediction = model.predict([[gender, age, hypertension, heart_disease, ever_married, avg_glucose_level, bmi, smoking_status]])

    
    if prediction[0] == 0:
        result = "Stroke"
    elif prediction[0] == 1:
        result = "Not a Stroke"
    else:
        result = "Unknown"

    return result

# Example usage
gender = 1
age = 67
hypertension = 0
heart_disease = 1
ever_married = 1
avg_glucose_level = 228.69
bmi = 36.6
smoking_status = 1

prediction_result = predict_stroke_result(gender, age, hypertension, heart_disease, ever_married, avg_glucose_level, bmi, smoking_status)
print(f"The prediction result is: {prediction_result}")