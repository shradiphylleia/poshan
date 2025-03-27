import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()
EMAIL_FROM=os.getenv("EMAIL")
PASSWORD=os.getenv("PASSWORD")

def mail_reminder(user_email:str,content:str,subject:str,date:str):
    """
    Sends an email reminder to the entered user_email of the given content and on the subject mentioned.
    
        content (str): The body of the email.
        subject (str): The subject of the email.
        user_email (str): The recipient's email address.
    """
    sender_password=PASSWORD
    msg=MIMEMultipart()
    msg["From"]=EMAIL_FROM
    msg["To"]=user_email
    msg["Subject"]=subject+" "+ date
    mail_content=content+" date to remmember:"+date
    msg.attach(MIMEText(mail_content,"plain"))
    try:
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.starttls() 
        server.login(EMAIL_FROM,sender_password)
        server.sendmail(EMAIL_FROM,user_email,msg.as_string())
        server.quit()
        print(f"reminder email sent to{user_email}")
    except Exception as e:
        print(f"Failed to send email:{e}")
