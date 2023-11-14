# import streamlit as st
# import pandas as pd

# @st.cache_data
# def load_data():
#     columns = ['manufacturer', 'model', 'drivetrain', 'price']  # Add all the columns you need
#     df = pd.read_csv('new_data_cars.csv', usecols=columns)
#     return df

# def filter_cars_by_price(df, min_price, max_price):
#     return df[(df['price'] >= min_price) & (df['price'] <= max_price)]

# def app():
#     st.title("Pricing Used Cars")
    
#     # Load the data
#     df = load_data()

#     st.image('photo.jpg', width=500, use_column_width=True)
#     st.subheader("***'We have data about the price for used cars obtained from a site for selling used cars'***")
       
#     st.header('***Put the range of the price and you will get [Manufacturer name, drivetrain, model]***')
   
#     # Define the price range
#     min_price = 260
#     max_price = 65500

#     # Create a slider for selecting the price range
#     selected_price_range = st.slider('Select Price Range', min_value=min_price, max_value=max_price, value=(min_price, max_price))

#     # Filter the car dataset based on the selected price range
#     filtered_cars = filter_cars_by_price(df, selected_price_range[0], selected_price_range[1])

#     # Display the filtered dataset
#     st.write(filtered_cars)

# # Run the app
# if __name__ == '__main__':
#     app()




import streamlit as st
import pandas as pd

# Load the data outside the app to avoid repeated reads
@st.cache
def load_data():
    columns = ['manufacturer', 'model', 'drivetrain', 'price']
    df = pd.read_csv('new_data_cars.csv', usecols=columns)
    return df

def filter_cars_by_price(df, min_price, max_price):
    return df[(df['price'] >= min_price) & (df['price'] <= max_price)]

def app():
    st.title("Pricing Used Cars")

    # Load the data
    df = load_data()

    # Resize the image to reduce load time
    st.image('photo.jpg', width=300, use_column_width=True)

    st.subheader("1. Delving into a dataset from a leading American used car sales site, my analysis uncovers key market trends and consumer behavior.")
    st.subheader("2. With a profound grasp of the business intricacies, I developed a cutting-edge predictive model leveraging machine learning to accurately forecast used car prices.")
    st.subheader("3. This model not only empowers users with informed decision-making but also enhances the overall transactional experience on the platform.")
    st.subheader("4. Elevating the site into a trusted destination, my work ensures reliable, data-driven transactions for both buyers and sellers alike.")


    # st.header('***Put the range of the price and you will get [Manufacturer name, drivetrain, model]***')

    # min_price = 260
    # max_price = 65500

    # selected_price_range = st.slider('Select Price Range', min_value=min_price, max_value=max_price, value=(min_price, max_price))

    # # Filter the DataFrame in memory
    # filtered_cars = filter_cars_by_price(df, selected_price_range[0], selected_price_range[1])

    # # Display the filtered DataFrame using st.dataframe for better performance
    # st.dataframe(filtered_cars)

# Run the app
if __name__ == '__main__':
    app()
