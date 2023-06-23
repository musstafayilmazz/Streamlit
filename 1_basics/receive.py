import streamlit as st

#Config the page must be first on streamlit

st.set_page_config(page_title='Demo',
                   page_icon="../santa-claus.png",
                   layout="centered",
                   initial_sidebar_state="collapsed")



st.title("Informations")
st.sidebar.success("Menu")
fname = st.text_input("Enter First Name")
sname = st.text_input("Enter Last Name")

password = st.text_input("Enter passowrd",type='password')

message = st.text_area("Please enter your comment")

number = st.number_input("Enter Number",1,25)

appointment = st.date_input("Appointment")

mytime = st.time_input("My Time")

color = st.color_picker("Select Color")