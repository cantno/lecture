import streamlit as st
import pandas as pd 
import plotly.express as px 

st.title("Streamlit Demo")
st.subheader("by M. K.")

df = px.data.iris()

st.write(df)

st.write(ox.scatter(df,x = "sepal_length",y="speal_width",color = "species"))
