import streamlit as st

st.title("hello Streamlit")

st.header("header")

st.subheader("sub header ")


st.text(" where are u from ")

st.markdown("""
# h1 tag 
## h2 tag 
### h3 tag 
:moon:<br>
:sunglasses:
**bold**
_italics_
""",True)

# st.latex(r'''

# ''')
b = { "name ": "priya",
        "age":24,
        "city":"bangalore"}

st.write( "# pawan")
st.write(sum)
st.write(b)
