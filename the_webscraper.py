import twilioauth as twauth

def main():
    tempsid = input("Enter your session ID : ")
    if tempsid != '':
        twauth.twiliodict['sid'] = tempsid
    
    tempauth = input("Enter your Twilio Auth : ")
    if tempauth != '':
        twauth.twiliodict['auth'] = tempauth
    
    temptwilphone = input("Enter your Twilio phone # : ")
    if temptwilphone != '':
        twauth.twiliodict['twilphone'] = temptwilphone
    
    tempuserphone = input("Enter your phone # to send to : ")
    if tempuserphone != '':
        twauth.twiliodict['userphone'] = tempuserphone
    for key in twauth.twiliodict:
        print(key, ",", twauth.twiliodict[key])
    
if __name__ == "__main__":
    main()
