import streamlit as st
st.image('poshan.png')
st.write("poshan is a chatbot which enables you to ask questions for personalized diet suggestions, diseases and set reminders")

st.subheader('food recommendations',divider=True)
st.image('food.png')
st.write('get personalized recommendations for diet')

st.subheader('health and joy',divider=True)
st.image('foodbowl.png')
st.write('get personalized recommendations for diet')

st.divider()
st.markdown("""Credits
- graphics for the app logo were sourced from [Canva](https://www.canva.com)
- emoji from [Emojis](https://emojis.wiki/reminder/), [Emojipedia](https://emojipedia.org/e-mail)
- speech to text [huggingface](https://huggingface.co)   
- built with [streamlit](https://streamlit.io/)
- gemini: for response model
""")

st.divider()
st.write("this project was created as part of a competition submission to AI/ML multi-track competition hosted by PeerHub x CIG IIT Roorkee")
st.write("the author is not a trained physian/ nutrionist therefore has little knowledge about the field. The app was made in good faith but can still have some errors. It is best to have your doctor step in at all times. Any error therefore is deeply regreted and is not intentional.")
st.write("by shraddha/shradiphylliea")
st.link_button("get in touch", "https://github.com/shradiphylleia")
