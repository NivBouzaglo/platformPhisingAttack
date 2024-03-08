import os
import time
import requests
import platform
from main import msg


def send_sms(mobile):
    from twilio.rest import Client


    account_sid = 'AC43d6ce649a8a890029c156a58803b346'
    auth_token = 'a426345baf7c7e7fe46ebca6d75a2fc7'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='+12403398347',
        body= msg,
        to=mobile
    )

    print(message.sid)
