import streamlit as st

import pandas as pd

df = pd.read_csv("../iris.csv")

#Show df
st.dataframe(df)
#Adding style to df
st.dataframe(df.style.highlight_max(axis=0))
#Show as static table
st.table(df)

#Show with super function
st.write(df.head())

# Display Json

st.json({'data' : 'name'})

#Display Code

mycode = """
def sayhello():
    print("Hello Streamlit)
"""

st.code(mycode)

