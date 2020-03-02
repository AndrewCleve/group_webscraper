# group_webscraper

IB CS group webscraper

## Installation

1. Clone the repository from github
2. Set up the virtual enviroment for the project in the root directory (the same folder as the [README.md](README.md) file) Make sure that you are using Python 3.8.x
3. Set up the virtual enviroment By running `/env/scripts/Activate`
4. Install the libraries with pip install `pip install -r requrements.txt`. This will install the libraries from the requrements file to ensure all contributers are using the same versions.
5. Create a python file called "twilioauth.py" with what's below inside. Change values to suit your needs.
```python
twiliodict = {'sid': 'My SID Here', 'auth': 'My Auth Here', 'twilphone': 'The Twilio Phone #', 'userphone': 'My Phone # here'}
```

##My Contributions
I mainly worked on the input section of the webscraper. This involved dealing with the entry fields of the GUI created by Jason. This meant that I wrote these lines to automatically put in default values for what and how often to scrape.
```python
        self.entWebsite.insert(0, "https://www.imdb.com/name/nm3485845/")
        self.entCheckRate.insert(0, "86400")
        self.entSID.insert(0, twauth.twiliodict["sid"])
        self.entAuth.insert(0, twauth.twiliodict["auth"])
        self.entTwilPhone.insert(0, twauth.twiliodict["twilphone"])
        self.entUserPhone.insert(0, twauth.twiliodict["userphone"])
```
The code above pulls from twauth.twiliodict, an array within the file twilioauth.py. The file is in the gitignore so that your personal twilio information doesn't get uploaded to github, and is imported in the imports section:
```python
import twilioauth as twauth
```
These entry fields are used to get the variables that change the scraped websites and how often it's to be checked, among other things.
```python
tempCheckRate = self.entCheckRate.get()
for i in range len(tempCheckRate):
    tempCheckRate.remove(",")

global userDictionary
userDictionary = {
    "websiteName": self.entWebsite.get(),
    "checkRate": tempCheckRate,
    "SID": self.entSID.get(),
    "twilioAuth": self.entAuth.get(),
    "twilioPhone": self.entTwilPhone.get(),
    "phoneNumber": self.entUserPhone.get(),
}
```
