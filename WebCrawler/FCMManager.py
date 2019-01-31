import MongoDBManager
import json
from firebase_admin import messaging

class FCM_Manager :

    def get_fcm_key(self) :
        with open('config.json', 'r') as file :
            config = json.load(file)
        return config["FCM"]["API_KEY"]

    def get_device_tokens(self) :
        return MongoDBManager.get_push_device_tokens()

    def __init__(self) :
        #Firebase Cloud Messaging Setting
        self.api_key = self.get_fcm_key()
        self.device_tokens = self.get_device_tokens()

