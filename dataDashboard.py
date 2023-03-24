import streamlit as st
import pandas

st.title("First Steamlit App")
st.subheader("Introducing Streamlit in Automate Everything with Python")
st.write("This is first Web App.")


data = {
	"Series 1":[1,2,3,4,5],
	"Series 2":[10,20,30,40,50]
}

df = pandas.DataFrame(data)

st.write(df)
st.line_chart(df)
st.area_chart(df)

myslider = st.slider("Celsius")
st.write(myslider, " Celsius in Fahrenheit is ", myslider *9/5 + 32)
