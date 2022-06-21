import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
import json
cred = credentials.Certificate("bobrlife-ec7da-firebase-adminsdk-on37f-2e7f4295e2.json")

default_app = firebase_admin.initialize_app(cred, {
	  'databaseURL': 'https://bobrlife-ec7da-default-rtdb.firebaseio.com',
    'storageBucket' : '/'
	})

