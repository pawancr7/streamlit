import streamlit as st 

st.title("Registration form")

first,last = st.columns(2)



first.text_input("First Name ")
last.text_input("Last Name")

email,mob = st.columns([3,1])
email.text_input("Email Id")
mob.text_input("Mob No")


user,pw,pw2 = st.columns(3)
user.text_input("User name ")
pw.text_input("pasword",type = "password")
pw2.text_input("retype your password",type ="password")


ch,bl,sub = st.columns(3)
ch.checkbox("I Agree ")
sub.button("submit")

