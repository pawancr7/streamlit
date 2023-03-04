import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt 
import time

plt.style.use("ggplot")

data = {
    "num":[x for x in range(1,11 )],
    "square":[x**2 for x in range(1,11)],
    "twice":[x*2 for x in range(1,11)],
    "thrice":[x*3 for x in range(1,11)]

}
sd = st.sidebar.radio("navigation",["home","aboutus"])
if sd == "home":

    df = pd.DataFrame(data)

    col = st.sidebar.multiselect("select a column",df.columns)
    plt.plot(df['num'],df[col])
    st.pyplot()
if sd == "aboutus":
    
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.1)
        progress.progress(i+1)

    st.balloons()




    
    st.success("show succes ")
    st.error("Error")
    st.info("information")
    st.exception(RuntimeError("this is an error "))
    st.warning("this is a warning ")

