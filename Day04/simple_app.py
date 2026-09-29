import streamlit as st
st.title("Welcome to my first app")
st.header("Home Page....")
st.subheader("About ....")
st.markdown("Hello **World**!")
st.chat_input("Enter your email")
name = st.text_input("Enter your name ...")


if st.button("Submit"):
    st.write("Hello",name)
