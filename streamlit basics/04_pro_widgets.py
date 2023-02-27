import streamlit as st 

st.title("WIDGETS")


if st.button("click here "):
    st.write("cristiano ronaldo siiiiiiiiiuuuuuuuuuuuu")

name = st.text_input("Name")
st.write(name)

addres = st.text_area("enter your text area ")
st.write(addres)


st.date_input("enter a date ")
st.time_input("enter a time ")
if st.checkbox("you accept the T&c",value=False):
    st.write("thank you ")

g1 = st.radio("colors",["r","b","g"],index = 0)

g2 = st.selectbox("Colors",["r","b","g"],index = 0)

st.write(g1,g2)

g4 = st.multiselect("Colors",["r","b","g"])
st.write(g4)

st.slider("age",min_value=10,max_value=80,value=30,step=2)
st.number_input("number",min_value=20,max_value=80,value=30,step=2)
img= st.file_uploader("upload here ")
st.image(img)