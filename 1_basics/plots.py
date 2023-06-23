import streamlit as st
#Additional packages
import pandas as pd
import numpy as np

#Data Load package
import plotly.express as px






st.title("Plotting")
df = pd.read_csv("../prog_languages_data.csv")
df.drop(["Unnamed: 0"],axis=1,inplace=True)
st.dataframe(df)

fig = px.pie(df,values="Sum",names="lang",title="Pie Chart")
st.plotly_chart(fig)

fig2 = px.bar(df,x="lang",y="Sum")
st.plotly_chart(fig2)