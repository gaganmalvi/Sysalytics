'''
Copyright (C) 2022 Gagan Malvi

Utility to send document reference from Firebase
'''

from firebase_admin import db
import firebase_admin

def send_doc_reference(env_path):
    # Parse environment variables the easy way
    envVars = []
    with open('.env', 'r') as f:
        envVars = f.read().splitlines()

    # Initialize Realtime Database
    databaseURL = envVars[0]
    cred = firebase_admin.credentials.Certificate(envVars[1])   

    default_app = firebase_admin.initialize_app(
        cred,
        {"databaseURL": databaseURL}
    )   

    # Set db reference to root
    dbRef = db.reference('/')

    return dbRef
