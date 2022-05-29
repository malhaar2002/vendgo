import pyrebase
import os
from django.shortcuts import render
 
config={
    "apiKey": "AIzaSyDOnL6kLVRhq50iaxrwNfF2rL19kxgx_II",
    "authDomain": "vendgo-2232a.firebaseapp.com",
    "databaseURL": "https://vendgo-2232a-default-rtdb.firebaseio.com",
    "projectId": "vendgo-2232a",
    "storageBucket": "vendgo-2232a.appspot.com",
    "messagingSenderId": "1003945059412",
    "appId": "1:1003945059412:web:cbe6825c937e60479139c1",
    "measurementId": "G-6BXQ8YJ152"
}

firebase=pyrebase.initialize_app(config)
auth = firebase.auth()

def create_user(email, password):
    auth.create_user_with_email_and_password(email, password)
    print("done")

def login_check(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        user = auth.refresh(user['refreshToken'])
        user_id = user['idToken']
        return True
        
    except:
        message = "Incorrect Password!"
        return False
