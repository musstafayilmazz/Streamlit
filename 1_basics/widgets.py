import streamlit as st

name = "Mustafa"
if st.button("Submit",key="mustafa"):
    st.write(f"Name -> {name.upper()}")

baco = "batu"
if st.button("Submit",key="batu"):
    st.write(f"Name -> {baco.upper()}")

status = st.radio("What is your status", ("Active","Inactive"))

if status == "Active":
    st.success("You are active")
else:
    st.error("Something is wrong")

#Checkbox

if st.checkbox("Show/Hide"):
    st.text("Showing Something")

#Expander
expanded = st.button("Python")
if expanded:
    st.success("Hello")

#Select/Multiple Select

my_lang = ["Python","Golang","C#","Java"]

choice = st.selectbox("Language",my_lang)

st.write(f"You choose {choice}")


#Working with media files
from PIL import Image
#IMAGE
img = Image.open("../image_01.jpg")
st.image(img,use_column_width=True)

st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/International_Pok%C3%A9mon_logo.svg/1200px-International_Pok%C3%A9mon_logo.svg.png")
#VIDEO
video_file = open("../secret_of_success.mp4","rb").read()
st.video(video_file)

#AUDIO

audio_file = open("../song.mp3","rb")
st.audio(audio_file)