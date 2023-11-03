import streamlit as st 
import pandas as pd 
import plotly.express as px

def app():
   st.title("Pricing Used Cars")

# Apply CSS styling to center the title
  

   st.image('photo.jpg', width=500,use_column_width=True)
   st.subheader("***'We have a data about the price for used cars and we got it from site for selling used cars'***")
       

   st.header('***Put the range of the price and you will get [Manufacturer name,drivetrian,model]***')
   range=st.button('Put The Range')
   df=pd.read_csv('new_data_cars.csv')
   

   # Function to filter the DataFrame based on price range
   def filter_cars_by_price(df, min_price, max_price):
      filtered_df = df[['manufacturer', 'model', 'drivetrain', 'price']]
      filtered_df = filtered_df[(filtered_df['price'].between(min_price, max_price))]
      return filtered_df
   
   # Define the price range
   min_price = 260
   max_price = 65500

   # Create a slider for selecting the price range
   selected_price_range = st.slider('Select Price Range', min_value=min_price, max_value=max_price, value=(min_price, max_price))

   # Filter the car dataset based on the selected price range
   filtered_cars = filter_cars_by_price(df, selected_price_range[0], selected_price_range[1])

   # Display the filtered dataset
   st.write(filtered_cars[['manufacturer', 'model', 'drivetrain', 'price']])


   


   

