import streamlit as st 

def app():
    st.title('My information ')
    number = st.button('Phon Number')
    if number :
        st.write('01010036764')
    linked = st.button('LinkedIn')
    if linked:
        st.write('https://www.linkedin.com/in/husseinalzeer7/')
    github = st.button('Github')
    if github:
        st.write('https://github.com/hussein199623')
    st.image('photo2.jpg', width=500,use_column_width=True)
