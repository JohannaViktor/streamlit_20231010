import streamlit as st
import pandas as pd
import numpy as np

st.write("Hello World!")
st.write("Hello again!")


a = st.sidebar.radio('Select one:', [1, 2])
if a==1:
    st.video("https://www.youtube.com/watch?v=qc-m3lIdD2c&t=19s")
else:
    st.write("and again")

col1, col2 = st.columns(2)
col1.write("This is column 1")
col2.write("This is column 2")

st.checkbox("I agree")
st.multiselect("Buy", ["milk", "apples", "potatoes"])
st.slider("Pick a number", 0, 100)
st.time_input("Meeting time")


DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

nrows=100
@st.cache_data
def load_data(DATA_URL_, nrows_):

    data = pd.read_csv(DATA_URL_, nrows=nrows_)
    data = data.rename(columns={"Lat": "LAT", "Lon": "LON"})
    return data
data = load_data(DATA_URL, nrows)
st.dataframe(data)
st.map(data.loc[:, ["LAT", "LON"]])