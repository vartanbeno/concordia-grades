from twilio.rest import Client
from env import MY_PHONE_NUMBER, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_NUMBER


client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


def text_myself(message):
    client.messages.create(body=message, from_=TWILIO_NUMBER, to=MY_PHONE_NUMBER)
