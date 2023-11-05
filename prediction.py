import streamlit as st
import pandas as pd
import numpy as np
import joblib

df = pd.read_csv('new_data_cars.csv')
tree = joblib.load('decision.pkl')
columns = joblib.load('columns.pkl')
manufacturer = joblib.load('manufacturer.pkl')
model = joblib.load('model.pkl')
engine = joblib.load('engine.pkl')
transmission = joblib.load('transmission.pkl')
drivetrain = joblib.load('drivetrain.pkl')
fuel_type = joblib.load('fuel_type.pkl')
exterior_color = joblib.load('exterior_color.pkl')
interior_color = joblib.load('interior_color.pkl')

def prediction(manufacturer, model, mileage, engine, Transmission,
              Drivetrain, fuel_type, mpg, Exterior_color, Interior_color,
              accidents_or_damage, one_owner, personal_use_only, year):
    data = pd.DataFrame(columns=columns)
    data.at[0, 'manufacturer'] = manufacturer
    data.at[0, 'model'] = model
    data.at[0, 'mileage'] = mileage
    data.at[0, 'engine'] = engine
    data.at[0, 'transmission'] = Transmission
    data.at[0, 'drivetrain'] = Drivetrain
    data.at[0, 'fuel_type'] = fuel_type
    data.at[0, 'mpg'] = mpg
    data.at[0, 'exterior_color'] = Exterior_color
    data.at[0, 'interior_color'] = Interior_color
    data.at[0, 'accidents_or_damage'] = accidents_or_damage
    data.at[0, 'one_owner'] = one_owner
    data.at[0, 'personal_use_only'] = personal_use_only
    data.at[0, 'year'] = year
    result = tree.predict(data)[0]
    return result

def app():
    st.title('Model Prediction')

    # Category columns
    Manufacturer = st.selectbox('Manufacturer', manufacturer)
    
    # Update available choices based on the selected manufacturer
    available_models = df[df['manufacturer'] == Manufacturer]['model'].unique()
    Model = st.selectbox('Model', available_models)
    
    available_engines = df[df['manufacturer'] == Manufacturer]['engine'].unique()
    Engine = st.selectbox('Engine', available_engines)

    available_drivetrain = df[df['manufacturer'] == Manufacturer]['drivetrain'].unique()
    Drivetrain = st.selectbox('DriveTrain', available_drivetrain)

    available_exterior_color = df[df['manufacturer'] == Manufacturer]['exterior_color'].unique()
    Exterior_color = st.selectbox('Exterior_color', available_exterior_color)

    available_interior_color = df[df['manufacturer'] == Manufacturer]['interior_color'].unique()
    Interior_color = st.selectbox('Interior_color', available_interior_color)

    available_transmission = df[df['manufacturer'] == Manufacturer]['transmission'].unique()
    Transmission = st.selectbox('Transmission', available_transmission)

    available_fuel_type = df[df['manufacturer'] == Manufacturer]['fuel_type'].unique()
    Fuel_type = st.selectbox('Fuel_type', available_fuel_type)

    # Continue with other selectboxes

    Year = st.slider('Year', min_value=1962, max_value=2023, step=1, value=1962)
    Mileage = st.slider('Mileage', min_value=4, max_value=200000, value=4, step=1)
    Mpg = st.slider('MPG', min_value=10, max_value=40, value=10, step=1)
    Accidents_or_damage = st.slider('Accidents or Damage', min_value=0, max_value=1, value=0, step=1)
    One_owner = st.slider('One Owner', min_value=1, max_value=1, value=0, step=1)
    Personal_use_only = st.slider('Personal Use Only', min_value=0, max_value=1, value=0, step=1)

    if st.button("Predict"):
        result = prediction(Manufacturer, Model, Mileage, Engine, Transmission,
                            Drivetrain, Fuel_type, Mpg, Exterior_color, Interior_color,
                            Accidents_or_damage, One_owner, Personal_use_only, Year)
        st.text(f"The predicted price is {result}")

if __name__ == '__main__':
    app()

