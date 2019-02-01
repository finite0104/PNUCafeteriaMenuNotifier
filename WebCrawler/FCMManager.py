import MongoDBManager
import json
from pyfcm import FCMNotification

class FCM_Manager :
    def _get_fcm_key(self) :
        with open('config.json', 'r') as file :
            config = json.load(file)
        return config["FCM"]["API_KEY"]

    def _get_device_tokens(self) :
        return MongoDBManager.get_push_device_tokens()

    def __init__(self) :
        #Firebase Cloud Messaging Setting
        self.api_key = self._get_fcm_key()
        self.device_tokens = self._get_device_tokens()
        self.push_service = FCMNotification(api_key=self.api_key)

    def send_fcm_message(self) :
        result = self.push_service.notify_multiple_devices(
            registration_ids=self.device_tokens,
            message_title='test_title',
            message_body='test_message',
        )

        print result