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
   # if range:
   #    def generate_visualizations(df):
   #          # Create a pie chart of manufacturer distribution
   #          manufacturer_counts = df['manufacturer'].value_counts()[:7]
   #          fig1 = px.pie(manufacturer_counts, values=manufacturer_counts.values, names=manufacturer_counts.index, 
   #                      title='Manufacturer Distribution')
   #          st.plotly_chart(fig1)
            
   #          # Create a histogram of price and model
   #          fig2 = px.histogram(df, x='price', y='model', nbins=10, title='Price Distribution',
   #                            labels={'price': 'Price', 'model': 'Model'})
   #          st.plotly_chart(fig2)
            
   #          # Create a scatter plot of drivetrain and price
   #          fig3 = px.bar(df, x='price', y='drivetrain',  title='Drivetrain vs. Price',
   #                         labels={'price': 'Price', 'drivetrain': 'Drivetrain'}, size_max=10)
   #          st.plotly_chart(fig3)

   #    # Read the dataset into a pandas DataFrame
   #    # df = pd.read_csv('dataset.csv')

   #    # Create a sidebar with price range slider
   #    st.title('Price Range')
   #    price_range = st.slider('Select Price Range', min_value=int(df['price'].min()), 
   #                                     max_value=int(df['price'].max()), value=(259, 65041))

   #    # Filter the data based on the price range
   #    filtered_data = df[(df['price'] >= price_range[0]) & (df['price'] <= price_range[1])]

   #    # Generate the visualizations
   #    generate_visualizations(filtered_data)

   

   def filter_cars_by_price(df, min_price, max_price):
      filtered_df = df[(df['price'] >= min_price) & (df['price'] <= max_price)]
      return filtered_df[['manufacturer', 'model', 'drivetrain', 'price']]

   # with columns: Manufacturer, Model, Drivetrain, and Price

   # Create a slider for selecting the price range
   min_price = 260
   max_price = 65500
   selected_price_range = st.slider('Select Price Range', min_value=min_price, max_value=max_price, value=(min_price, max_price))

   # Filter the car dataset based on the selected price range
   filtered_cars = filter_cars_by_price(df, selected_price_range[0], selected_price_range[1])

   # Display the filtered dataset
   st.write(filtered_cars)

   


   

