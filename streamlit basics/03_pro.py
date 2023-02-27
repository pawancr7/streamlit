import streamlit as st
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import graphviz

data = pd.DataFrame(
    np.random.randn(100,3),
    columns=['a','b','c']
)

plt.scatter(data['a'],data['b'])
plt.title("scatter chart ")
st.pyplot()
st.line_chart(data,width=400)

st.area_chart(data)

st.bar_chart(data)

st.map()

st.graphviz_chart("""
digraph{
watch -> like 
like -> subscribe 
subscribe -> share }
""")

st.image("483704.jpg",width=400)
st.audio("soft.wav")

st.video("https://www.youtube.com/watch?v=Tc-XxqEyolU")