import streamlit as st 
import pandas as pd 
import seaborn as sns
import plotly.express as px 
import matplotlib.pyplot as plt 


def app():
    st.title('Data Analysis')
    df=pd.read_csv('new_data_cars.csv')

    st.header('Bar chart')
    st.subheader('***How many transimission in each manufacturer, and who has the most option***')
    trans_number= df.groupby('manufacturer')['transmission'].nunique().to_frame().reset_index().sort_values(by='transmission',ascending=False)

    # fig=plt.figure(figsize=(20,10))
    fig=px.bar(trans_number,x='transmission',y='manufacturer',color=trans_number['transmission'])
    # plt.title('Number of transmission in each manufacturer',fontsize=26)
    st.plotly_chart(fig)
    st.write('1- the most manufacturer has bigest number of are Kia=35 and Ford=35 kind of transmissions, so they have beggest number fo options')
    st.write('2- on the other hand Tsla and RAM has the lowest number of transmission Tesla = 5 and RAM=13')


    st.subheader('***what is the avg price for each manufacturer***')
    
    # fig= plt.figure(figsize=(9,5))
    pric= df.groupby('manufacturer')['price'].mean().round(2).sort_values(ascending=False).reset_index()
    fig=px.bar(y=pric['manufacturer'],x=pric['price'],color=pric['manufacturer'])
    st.plotly_chart(fig)
    st.write('1- So Tesla and Land Rover has the heigest price')
    st.write('2- The ecounmic cars like Nissan and Hyundai and Mezda')

    st.header('Heatmap')
    st.subheader('***waht is the most factor have an effect on the price of the car***')
    fig=plt.figure(figsize=(10,10))
    cor=df.select_dtypes('number')
    sns.heatmap(cor.corr(),annot=True)
    st.pyplot(fig)
    
    st.write('1-We have a negative relationship between price and mileage, so the more mileage the lower the price  ')
    st.write('2- We have a positive relation between price and year, So the more years, the higher the price')
    
    st.header('Pie chart')
    st.subheader('***what is the avg price for eahc drivetrain***')
    avg_price_drivetrain = df.groupby('drivetrain')['price'].mean().round(2).to_frame().reset_index().sort_values(by='price',ascending=False)
    fig=px.pie(data_frame=avg_price_drivetrain,names='drivetrain',values='price')
    st.plotly_chart(fig)

    st.write('1- Front wheels drive are the cheabest price')
    st.write('2- Four wheels and All wheels drive are have the higest price ')
    
    st.header('Histogram')
    st.subheader('***what is the most three popular transmission and there price*** ')
    trans=  df[df['transmission'].isin(['Automatic CVT', '6-Speed Automatic', '8-Speed Automatic'])]
    trans=trans.groupby('transmission')['price'].mean().to_frame().reset_index()
    # fig=px.pie(names=trans['transmission'],values=trans['price'],)
    fig=px.histogram(trans,x='transmission',y='price',histfunc='avg')
    st.plotly_chart(fig)
    

    st.write('her is the most popular kinds of transmission and there prices')
    st.write(trans)

    st.header('Line Chart')
    st.subheader('what is the rate of chang in the price over years')
    fig = plt.figure(figsize=(15, 6))

# Plot the data
    sns.lineplot(x=df['year'],y= df['price'], marker='*',lw=2, ls='-', c='red')

    # Set labels and title
    plt.ylabel('Price')
    plt.xlabel('Year')
    plt.title('Car Price over Time')

    # Display the plot using Streamlit
    st.pyplot(fig)





    # the dream funcation 


    # def generate_visualizations(df):
    #     # Create a pie chart of manufacturer distribution
    #     manufacturer_counts = df['manufacturer'].value_counts()[:7]
    #     fig1, ax1 = plt.subplots()
    #     ax1.pie(manufacturer_counts, labels=manufacturer_counts.index, autopct='%1.1f%%', startangle=90)
    #     ax1.axis('equal')
    #     plt.title('Manufacturer Distribution')
    #     st.pyplot(fig1)
        
    #     # Create a histogram of price and model
    #     fig2, ax2 = plt.subplots()
    #     ax2.hist(df['price'], bins=10)
    #     ax2.set_xlabel('Price')
    #     ax2.set_ylabel('Count')
    #     ax2.set_title('Price Distribution')
    #     st.pyplot(fig2)
        
    # #     # Create a scatter plot of drivetrain and price
    #     fig3, ax3 = plt.subplots()
    #     ax3.scatter(df['drivetrain'], df['price'])
    #     ax3.set_xlabel('Drivetrain')
    #     ax3.set_ylabel('Price')
    #     ax3.set_title('Drivetrain vs. Price')
    #     st.pyplot(fig3)

    # # # Read the dataset into a pandas DataFrame
    

    # # # Create a sidebar with price range slider
    # st.title('Inter the Price Range to get info about ***Manufacturer -price -model- drivetrain***')
    # price_range = st.slider('Select Price Range', min_value=int(df['price'].min()), 
    #                                 max_value=int(df['price'].max()), value=(259, 65041))

    # # # Filter the data based on the price range
    # filtered_data = df[(df['price'] >= price_range[0]) & (df['price'] <= price_range[1])]

    # # # Generate the visualizations
    # generate_visualizations(filtered_data)




    
