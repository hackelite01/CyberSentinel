import streamlit as st
from PIL import Image

hide_menu = """
<style>
#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}
</style>
"""

showWarningOnDirectExecution = False
image = Image.open('icons/logo.png')
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("Hey I'am Mayank Rajput")  
st.markdown(" <br> ", unsafe_allow_html=True)
st.markdown("This Project focuses on :blue[**_Cyber Bullying Detection Application is a Machine Learning Web application for Cyber Bullying Detection_**]. The aim is to leverage advanced machine Learning techniques to detect and prevent cyberbullying incidents in online communications.")
st.markdown(" <br> ", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br> <br> <br>", unsafe_allow_html=True)

st.set_page_config(page_title = "CyberSentinel", page_icon = image)

st.markdown(hide_menu, unsafe_allow_html=True)

st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.image(image , use_column_width=True, output_format='auto')


st.sidebar.markdown("---")


st.sidebar.markdown("<br> <br> <br> <br> <br> <br> <h1 style='text-align: center; font-size: 18px; color: #0080FF;'> © 2024 | hackelite01 </h1>", unsafe_allow_html=True)

st.image(image , use_column_width=True)
