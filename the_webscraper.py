import twilio
from twilio.rest import Client
import twilioauth as twauth
import tkinter as tk

window = tk.Tk()


class GUI:
    def RunGUI(self):

        l1 = tk.Label(window, text="Enter website name here ")
        l2 = tk.Label(window, text="Enter checkrate here (in seconds) ")
        l3 = tk.Label(window, text="Enter SID here ")
        l4 = tk.Label(window, text="Enter Twilio Authorization here ")
        l5 = tk.Label(window, text="Enter Twilio phone number here ")
        l6 = tk.Label(window, text="Enter user phone number here ")

        self.entWebsite = tk.Entry(window, text="Hello World")
        self.entCheckRate = tk.Entry(window)
        self.entSID = tk.Entry(window)
        self.entAuth = tk.Entry(window)
        self.entTwilPhone = tk.Entry(window)
        self.entUserPhone = tk.Entry(window)

        self.entWebsite.insert(0, "https://www.imdb.com/name/nm3485845/")
        self.entCheckRate.insert(0, "86400")
        self.entSID.insert(0, twauth.twiliodict["sid"])
        self.entAuth.insert(0, twauth.twiliodict["auth"])
        self.entTwilPhone.insert(0, twauth.twiliodict["twilphone"])
        self.entUserPhone.insert(0, twauth.twiliodict["userphone"])

        button = tk.Button(window, text="Finish", width=25, command=self.end)

        l1.grid(row=0, column=0, pady=2)
        l2.grid(row=1, column=0, pady=2)
        l3.grid(row=2, column=0, pady=2)
        l4.grid(row=3, column=0, pady=2)
        l5.grid(row=4, column=0, pady=2)
        l6.grid(row=5, column=0, pady=2)

        self.entWebsite.grid(row=0, column=2, pady=2)
        self.entCheckRate.grid(row=1, column=2, pady=2)
        self.entSID.grid(row=2, column=2, pady=2)
        self.entAuth.grid(row=3, column=2, pady=2)
        self.entTwilPhone.grid(row=4, column=2, pady=2)
        self.entUserPhone.grid(row=5, column=2, pady=2)

        button.grid(row=6, column=1)

        window.mainloop()

    def end(self):

        # stationdictionary.update({elevation : name})

        global userDictionary
        userDictionary = {
            "websiteName": self.entWebsite.get(),
            "checkRate": self.entCheckRate.get(),
            "SID": self.entSID.get(),
            "twilioAuth": self.entAuth.get(),
            "twilioPhone": self.entTwilPhone.get(),
            "phoneNumber": self.entUserPhone.get(),
        }

        print(userDictionary)

        # big credit to Andrew for like.. figuring it out, thanks Java
        window.destroy()


def output(change_message):
    twilio_sid = twauth.twiliodict["twilio_sid"]
    twilio_auth = twauth.twiliodict["twilio_auth"]
    twilio_phone = twauth.twiliodict["twilio_phone"]
    user_phone = twauth.twiliodict["user_phone"]
    # print(twilio_sid, twilio_auth, twilio_phone, user_phone, message)
    client = Client(twilio_sid, twilio_auth)
    message = client.messages.create(
        body=change_message, from_=twilio_phone, to=user_phone
    )
    print(message.sid)


if __name__ == "__main__":
    firstGUI = GUI()
    firstGUI.RunGUI()
