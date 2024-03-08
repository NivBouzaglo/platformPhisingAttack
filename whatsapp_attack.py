
import pywhatkit as kit
from datetime import datetime, timedelta
from main import msg

from twilio.rest import Client



def whatsapp_atk(mobile):
    # message = "Hello from Python! This is an instant WhatsApp message."

    # Get current time
    now = datetime.now() + timedelta(minutes=1)
    current_hour = now.hour
    current_minute = now.minute
    mobile = "+972" + mobile[1:]

    # Send the message instantly
    kit.sendwhatmsg(
        phone_no=mobile,
        message=msg,
        time_hour=current_hour,
        time_min=current_minute
    )

    print(" WhatsUp Attack : The message was sent successfully ")



def whatsapp_atk_using_twilio(mobile):
    from twilio.rest import Client


    account_sid = 'AC43d6ce649a8a890029c156a58803b346'
    auth_token = 'a426345baf7c7e7fe46ebca6d75a2fc7'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body= msg,
        to='whatsapp:'+mobile
    )

    print(message.sid)

    # """ ********************************************** """
