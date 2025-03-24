import streamlit as st

st.title("poshan")
st.logo("poshan.png",size='large')
pages={
    "General":[st.Page("about.py",title="poshan")],
    "chatbot":[st.Page("chat.py",title="poshan chatbot")]
}

pg=st.navigation(pages)
pg.run()


