""" 
Matthew Thompson
05/12/2023
Automatically check for new files in a folder and send a notification
"""

import os
import time
import smtplib
from plyer import notification

folder_paths = ['c:\\dev\\python\\', 'c:\\dev\\python\\new']
smtp_server = 'smtp.yoursite.com'
smtp_port =  587
email_login = 'your.email@yoursite.com'
email_password = 'yourpassword'
sender = 'sender@yoursite.com'
receiver = 'receiver@yoursite.com'
subject = "New File Added to Your Watched Folder"
body = "A new file has been added to your watched folder."

def send_email_notification():
    message = f'From: {sender}\nTo: {receiver}\nSubject: {subject}\n\n{body}'
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(email_login, email_password)
    server.sendmail(sender, receiver, message)
    server.quit()

def send_desktop_notification():
    notification.notify(
        title='New SAS Dataset Added',
        message='A new SAS dataset has been added to the folder.',
        timeout=5
    )

def check_for_new_files():
    for folder_path in folder_paths:
        current_files = set(os.listdir(folder_path))
        time.sleep(10) # wait for 10 seconds
        new_files = set(os.listdir(folder_path)) - current_files
        if new_files:
            try:
                send_email_notification()
            except Exception as e:
                print(f'Email notification failed with error: {e}')
                send_desktop_notification()

while True:
    check_for_new_files()