import streamlit as st
import pandas as pd 
import numpy as np 

a = [1,2,3,4,5,6,7,8]
n = np.array(a)
nd = n.reshape((2,4))
# print(nd)
dic = {
    "name":"pawan",
     "age":24,
     "city":"delhi"
    }
data = pd.read_csv("Salary_Data.csv")

st.dataframe(data,  width=400,height=500)
st.table(dic)
st.write(data)
st.json(dic)





