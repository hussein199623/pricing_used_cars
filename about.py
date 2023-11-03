import streamlit as st 
import pandas as pd 



def app():
    st.title('Pricing Used cars')
    link = st.button('The link of the data')
    if link :
        st.write('https://www.kaggle.com/datasets/andreinovikov/used-cars-dataset')
    st.subheader('We have a dataset about price of used cars ')
    data=st.button('Show data')
    df = pd.read_csv("new_data_cars.csv")
    st.write('I used model DecsisionTree, I achieved 92% accuracy)
    if data :
        st.write('Here are 10 rows of the data to give you fast intuition)
        st.dataframe(df.sample(10))
    
    meta_data = st.button('Metadata & Description of the data')
   

    description = {'manufacturer': 'name of the car manufacturer',
    'model': 'name of the car model',
    'year': 'the year when the car was produced',
    'mileage': 'the number of miles the car has traveled since production',
    'engine': 'car engine',
    'transmission': "type of the car's transmission",
    'drivetrain': "type of the car's drivetrain",
    'fuel type': 'type of fuel that the car consumes',
    'mpg': 'the number of miles a car can travel using one gallon of fuel (miles per gallon)',
    'exterior color': 'car exterior color',
    'interior color': 'car interior color',
    'accidents or damage': 'whether the car was involved in accidents',
    'one owner': 'whether the car was owned by one person',
    'personal use only': 'whether the car was used only for personal purposes',
    'seller name': 'name of the seller',
    'seller rating': "seller's rating",
    'driver rating': 'car rating is given by drivers',
    'driver reviews num': 'the number of car reviews left by drivers',
    'price drop': 'price reduction from the initial price',
    'price': 'car price'}
    if meta_data:
        st.write('Columns description ')
        st.table(description)
