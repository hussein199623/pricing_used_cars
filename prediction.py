
import streamlit as st 
import pandas as pd 
import numpy as np 
import seaborn as sns
import joblib 
 

# st.title('Pricing Used cars')

# forest =joblib.load('random.pkl')
tree = joblib.load('decision.pkl')
columns= joblib.load('columns.pkl')
manufacturer = joblib.load('manufacturer.pkl')
model= joblib.load('model.pkl')
engine=joblib.load('engine.pkl')
transmission = joblib.load('transmission.pkl')
drivetrain = joblib.load('drivetrain.pkl')
fuel_type = joblib.load('fuel_type.pkl')
exterior_color = joblib.load('exterior_color.pkl')
interior_color = joblib.load('interior_color.pkl')

def prediction(manufacturer, model, mileage, engine, transmission,
       drivetrain, fuel_type, mpg, exterior_color, interior_color,
       accidents_or_damage, one_owner, personal_use_only, year):
       data=pd.DataFrame(columns=columns)
       data.at[0,'manufacturer']=manufacturer
       data.at[0,'model']= model
       data.at[0,'mileage']=mileage
       data.at[0,'engine']=engine
       data.at[0,'transmission']=transmission
       data.at[0,'drivetrain']= drivetrain
       data.at[0,'fuel_type']= fuel_type
       data.at[0,'mpg']= mpg
       data.at[0,'exterior_color']=exterior_color
       data.at[0,'interior_color']=interior_color
       data.at[0,'accidents_or_damage']=accidents_or_damage
       data.at[0,'one_owner']=one_owner
       data.at[0,'personal_use_only']=personal_use_only
       # data.at[0,'price']=price
       data.at[0,'year']=year
       result=tree.predict(data)[0]
       return result

def app():
       # title
       st.title('Model Prediction')
       ## category columns 
       Manufacturer = st.selectbox('Manufacturer',list(manufacturer))
       Model= st.selectbox('Model',list(model))
       Engine = st.selectbox('Engine',list(engine))
       Transmission = st.selectbox('Transmission',list(transmission))
       Drivetrain = st.selectbox('DraiveTrain',list(drivetrain))
       Fuel_type = st.selectbox('Fuel_Type',list(fuel_type))
       Exterior_color =st.selectbox('exterior_color',list(exterior_color))
       Interior_color= st.selectbox('interior_color',list(interior_color))
       # numeric columns 
       Year= st.slider('year',min_value=1962,max_value=2023,step=1,value=1962)
       Mileage=st.slider('Mileage',min_value=4,max_value=200000,value=4,step=1)
       Mpg=st.slider('Mpg',min_value=10,max_value=40,value=10,step=1)
       Accidents_or_damage=st.slider('Accidents_or_damage',min_value=0,max_value=1,value=0,step=1)
       One_owner=st.slider('One_owner',min_value=1,max_value=1,value=0,step=1)
       Personal_use_only=st.slider('Personal_use_only',min_value=0,max_value=1,value=0,step=1)
       
       if st.button("prediction"):
              result = prediction(Manufacturer, Model, Mileage, Engine, Transmission,
              Drivetrain, Fuel_type, Mpg, Exterior_color, Interior_color,
              Accidents_or_damage, One_owner, Personal_use_only,Year)
              st.text(f"The Price will be {result}")

if __name__ == '__main__':
       app()


