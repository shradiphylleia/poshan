# poshan
submission to AI/ML Multi-Track Competition By PeerHub x CIG IIT Roorkee
round 3 health_track_chatbot
1. diet suggestion based on age and gender: suggesting personalized diet plans based on calorie intake and health goals
2. Answer disease-related queries (database)
3. Send automated health reminders(need email:which triggers some python script to send a mail with the said reminder)


# Setting up locally
1.  Run: pip install -r requirements.txt to get the required libs working
2. create .env in the root dir with 
EMAIL=email@domain.com
PASSWORD=app password(recommended,please refrain from adding personal password)
3. to launch the ui enter the below in cmd/terminal:
run streamlit landing.py



# milestone marker
---internal milestone refernce puropse only----
# goal[23 march,2025]
1. working prototype which has chat feature(done)
2. find database(done)
3. script(isolated to send email) integrate with frontend(done)

# goal[24 march,2025]
1. make responses better--chances of typo(almost 26 march)
2. setup the mailing function(done,26 march)
3. taking audio input.(done,26 march)


# goal[25 march,2025]
1. google translate to support multilingual support(done 26 march)
2. login and auth to save email details