# Core Package
import streamlit as st
import string

#Additional Packages

# Funcs

def main():
    """All Of The Codes will be here"""
    st.title("First App")
    st.text("In this section we will develop apps")

    st.header("This is my header")
    #Colors
    st.success("Succesful")
    st.warning("Error")
    st.info("Information given")
    st.error("Error accuared")
    st.exception("An exception")

    #Super Function
    st.write("## This is a test")
    st.write(2+5)

    st.help(type)

    st.write(dir(st))

if __name__ == '__main__':
    main()