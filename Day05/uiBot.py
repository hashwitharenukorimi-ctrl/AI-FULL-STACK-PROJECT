import ollama
import streamlit as st
st.title(":violet[AstraBot🤖!!!]")
with st.sidebar:
    personalities = {
        "Kid👶" : "Give the answers like you are explaining to a 5year old kid .Give the answer in 2 lines only",
        "Professor🧑‍🏫": "You are an IIT professor. Explain the topics using correct terminology. Give the answer in 2 lines only ",
        "Student👩‍🎓" : "You are student in btech college .explain the topics using correct terminology as a btech student.give the answer in 2 lines only"
    }
    personality = st.selectbox("Select a personality",personalities.keys())
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.success("Chat cleared successfully🚮")
    st.header("Chat Settings⚙️")
    uploaded_file = st.file_uploader("Upload a file.....")
    try:
        if uploaded_file:
            st.write("File uploaded successfully🗄️......")
            with st.expander("Preview"):
                context = uploaded_file.read().decode("utf-8")
                st.text(context)
    except:
            st.error("File type not supported")
if "messages" not in st.session_state:
    st.session_state.messages = []
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
question = st.chat_input("You : ")
if question:
    with st.chat_message("User"):
        st.write("User: ",question)
    
    st.session_state.messages.append(
        {
            "role" : "user",
            "content" : question
        }
    )
    with st.spinner("Thinking......"):
        response = ollama.chat(
            model="llama3.2:3b",
            messages =[{
                "role": "system","content" : personalities[personality]
            }] + st.session_state.messages
        )
    st.session_state.messages.append(
            {
                "role" : "assistant",
                "content":response["message"]["content"]
            }
        ) 
    with st.chat_message("Assistant"):
        st.write("AI:",response["message"]["content"])




