import streamlit as st

from streamlit_option_menu import option_menu


import home, analysis, prediction, about, account
st.set_page_config(
        page_title="Main Menu",
)
pages = ['Home', 'Account', 'About', 'Analysis', 'Prediction']

# Get the selected page from the URL parameter
selected_page = st.experimental_get_query_params().get('page', ['Home'])[0]

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='Main Menu ',
                options=['Home','Account','About','Analysis','Prediction'],
                icons=['house-fill','person-circle','info-circle-fill','chat-fill','trophy-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "red"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )

        
        if app == "Home":
            home.app() 
        if app == "Account":
            account.app() 
        if app == 'About':
            about.app()   
        if app == "Analysis":
            analysis.app()        
        if app == 'Prediction':
            prediction.app()
           
             
          
             
    run()            
         