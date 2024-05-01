import streamlit as st
from streamlit_chat import message

def main():
    st.title("My Chatbot")
    msgs = []

    with st.form("chat_form"):
        user_input = st.text_input("You:", key="user_input")
        submit_button = st.form_submit_button("Send")

        if submit_button:
            # Process the user input and generate a response
            response = "Hello! This is a sample response."
            msgs.append(message("You: " + user_input))
            msgs.append(message("Bot: " + response))

    st.chat(msgs)

if __name__ == "__main__":
    main()
