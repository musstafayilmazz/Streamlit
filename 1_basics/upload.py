import streamlit as st

from PIL import Image
import pandas as pd
import docx2txt
import pdfplumber
from PyPDF2 import PdfFileReader

@st.cache_data
def load_image(image_file):
    img = Image.open(image_file)
    return img

def read_pdf(file):
    pdfReader = PdfFileReader(file)
    count = pdfReader.numPages
    all_page_text = " "
    for i in range(count):
        page = pdfReader.getPage(i)
        print(page)
        all_page_text += page.extractText()
    return all_page_text

def uploader(header,imagetype):
    file = st.file_uploader(header,type=imagetype)
    if st.button("Process"):
        if file is not None:
            #st.write(type(file))
            #st.write(dir(file))
            try : 
                file_details = {
                "file class" : file.__class__,
                "file name" : file.name,
                "file_type" : file.type,
                "buffer" : file.getbuffer
            }
                st.write(file_details)
            except:
                pass
            return file
    

st.title("Upload")

menu = ["Home","Dataset","DocumentFiles","About"]
choice = st.sidebar.selectbox("Menu",menu)
match choice:
    case "Home":
        st.subheader("Home")
        img = uploader("Image Files",["png","jpg","jpeg"])
        st.image(load_image(img))
    
    case "Dataset":
        st.subheader("Dataset")
        dataset = uploader("Data File",["csv"])
        df = pd.read_csv(dataset)
        st.dataframe(df)
    
    case "DocumentFiles":
        st.subheader("DocumentFiles")
        documents = uploader("Documents",["pdf","docx","txt"])
        if documents.type == "text/plain":
            text = str(documents.read(),"utf-8")
            st.write(text)
        elif documents.type == "application/pdf":

            text = read_pdf(documents)
            st.write(text)

            

        else:
            text = docx2txt.process(documents)
            st.write(text)
            st.text(text)
        

 


    
    case "About":
        st.subheader("About")