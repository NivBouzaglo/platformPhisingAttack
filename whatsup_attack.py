""" TODO : this library opens the whatsup and sends it to the receiver, means that we cant use a fake number
           if we wish to use another number we need to use twilio but we need to pay money :(  """

import pywhatkit as kit

# Specify the phone number (with country code) and the message

message = "Hello from Python! This is an instant WhatsApp message."

# Send the message instantly
kit.sendwhatmsg(
    phone_no="+972584785548",
    message="This is a scheduled message.\nhttps://ticketsforyou.000webhostapp.com/",
    time_hour=16,
    time_min=27
)

print(" WhatsUp Attack : The message was sent successfully ")


""" The code using Twilio """
""" ********************************************** """
# from twilio.rest import Client
#
# # Twilio credentials
# account_sid = 'AC224543ae20f0be827de1306c93a5872f'
# auth_token = '083414fcc2ca339e47af0ce1ab18b561'
# twilio_phone_number = '+14155238886'  # Your Twilio phone number
#
# # Recipient's phone number (including country code)
# recipient_phone_number = '+972584785548'
#
# # Message to send
# message_body = "Its working"
#
# # Initialize Twilio client
# client = Client(account_sid, auth_token)
#
# # Send WhatsApp message
# message = client.messages.create(
#     from_='whatsapp:' + twilio_phone_number,
#     body=message_body,
#     to='whatsapp:' + recipient_phone_number
# )
#
# print("Message sent successfully!")

""" ********************************************** """
