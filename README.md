# poshan
submission to AI/ML Multi-Track Competition By PeerHub x CIG IIT Roorkee
round 3 health_track_chatbot
1. diet suggestion based on age and gender: suggesting personalized diet plans based on calorie intake and health goals
2. Answer disease-related queries (database)
3. Send automated health reminders(need email:which triggers some python script to send a mail with the said reminder)


# Setting up locally
1. Prerequisites
Ensure you have Python installed on your system. If not, download and install it from [python.org](https://www.python.org/downloads/).

## Installation Steps

1. Clone the Repository

2. Install Dependencies
   Run the following command to install the required libraries:
   ```sh
   pip install -r requirements.txt
   ```

3. Set Up Environment Variables
   Create a `.env` file in the root directory and add the following details:
   ```env
   EMAIL=email@domain.com
   PASSWORD=your_app_password  # Use an app-specific password, not a personal one
   API_KEY=your_gemini_api_key  # Obtain this from the Gemini API provider
   ```

4. Create FAQ Data File
   Ensure a JSON file named `medical_chatbot_conversations.json` exists in the root directory. Format it according to your specifications for FAQs.
   format:
   ```
     [  {
        "messages": [
            {
                "role": "user",
                "text": "What does this website do?"
            },
            {
                "role": "bot",
                "text": "This website is your personal guide to health and fitness! Whether you're looking for workout plans, nutrition advice, or wellness tips, we've got you covered."
            }
        ]
    }, ]
   ```

6. Rename Response Model File
   Change the extension of `response_model.md` to response_model.py

7. Launch the UI
   Run the following command in the terminal:
   ```sh
   streamlit run landing.py
   ```

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
2. login and auth to save email details(on hold)

# goal[28 march,2025]
1. sos email--need auth
