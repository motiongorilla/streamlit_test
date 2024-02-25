import streamlit as st
import pandas

data = {
        'Series_1':[1,3,4,5,7,999],
        'Series_2':[10,3,59,100,231,123],
        'Series_3':[1,5,6,2,25,6]
        }

df = pandas.DataFrame(data)

st.title("First Streamlit app")
st.subheader("Checking out streamlit workflow")
st.write("Updated text just to see if the update is going to come through!")

st.write(df)

