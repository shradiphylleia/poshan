import streamlit as st
import time
import re
from mail_button import set_mail_reminder as reminder_btn
from json_loader import load_json

json_data=load_json()
 
def get_response_json(user_query):
    for conv in json_data:
        for msg in conv["messages"]:
            if msg["role"]=="user":
                pattern=re.compile(re.escape(msg["text"]),re.IGNORECASE)
                if pattern.search(user_query):
                    return next((m["text"] for m in conv['messages'] if m['role']=='bot'),"Currently, unable to respond.poshan is in the works")
    return "Currently, unable to respond.poshan is in the works"


def rsp(response):
    for word in response.split():
        yield word + " "
        time.sleep(0.25)



st.write("poshan is a chatbot which enables you to ask questions for personalized diet suggestions, diseases and set reminders")
st.button(label='reminder 📨', on_click=reminder_btn)

# if no session histroy we reate a list and append to it
if "msgs" not in st.session_state:
    st.session_state.msgs=[]

# dict like role and the contents of the msg
for msg in st.session_state.msgs:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# take the prompt & if the prompt is !none 
if prompt:=st.chat_input("ask your query.."):
    st.chat_message("user").markdown(prompt)
    st.session_state.msgs.append({"role":"user","content":prompt})

    ai_response=get_response_json(prompt)

    with st.chat_message('ai'):
        response=st.write_stream(rsp(ai_response))
    st.session_state.msgs.append({'role':'ai','content':response})
