import twilio
from twilio.rest import Client


def output(change_message, user_config):
    twilio_sid = user_config["twilio_sid"]
    twilio_auth = user_config["twilio_auth"]
    twilio_phone = user_config["twilio_phone"]
    user_phone = user_config["user_phone"]
    # print(twilio_sid, twilio_auth, twilio_phone, user_phone, message)
    client = Client(twilio_sid, twilio_auth)
    message = client.messages.create(
        body=change_message, from_=twilio_phone, to=user_phone
    )
    print(message.sid)
