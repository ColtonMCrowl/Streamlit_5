import streamlit as st

st.title("My Streamlit App")

# 2 columns to display text.
col1, col2 = st.columns(2)

#Column 1 with the text "Hello"
col1.write("Hello")

#Column 2 with the text "World"
col2.write("World")

#An expander that reveals text when clicked
with st.expander("Click me"):
    st.write("Here you could put in some really, really explanatory stuff.")
