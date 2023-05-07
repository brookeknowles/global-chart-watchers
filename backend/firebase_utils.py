"""
Setup and configuration of the firebase firestore db
"""

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Firebase db setup
cred = credentials.Certificate('global-chart-watchers-firebase-adminsdk-av0zu-8c70f19b28.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
