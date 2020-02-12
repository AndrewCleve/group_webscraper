import twilio
from twilio.rest import Client
import twilioauth as twauth


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


def main():
    tempsid = input("Enter your session ID : ")
    if tempsid != "":
        twauth.twiliodict["sid"] = tempsid

    tempauth = input("Enter your Twilio Auth : ")
    if tempauth != "":
        twauth.twiliodict["auth"] = tempauth

    temptwilphone = input("Enter your Twilio phone # : ")
    if temptwilphone != "":
        twauth.twiliodict["twilphone"] = temptwilphone

    tempuserphone = input("Enter your phone # to send to : ")
    if tempuserphone != "":
        twauth.twiliodict["userphone"] = tempuserphone
    for key in twauth.twiliodict:
        print(key, ",", twauth.twiliodict[key])


if __name__ == "__main__":
    main()
