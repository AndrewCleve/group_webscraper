import requests
from bs4 import BeautifulSoup
import time

numberOfCredits = ""
def magic_happens():
    #url = "https://www.imdb.com/name/nm3485845/?ref_=fn_al_nm_1" #website
    url = userDictionary["websiteName"]
    response = requests.get(url) #get html from site
    soup = BeautifulSoup(response.content,"html.parser") #add html to BeautifulSoup
    div = soup.find(id = "filmo-head-actor" ) #search soup for tag h1\
    
    unwanted = div.find('span') #remove stuff
    unwanted.extract()
    unwanted = div.find('span')
    unwanted.extract()
    unwanted = div.find('a')
    unwanted.extract()
    str = div.text
    newStr = str.replace("(", " ")
    newestStr = newStr.replace(")", " ")
    
    
    if numberOfCredits == "":
        numberOfCredits = newestStr
    elif numberOfCredits != newestStr:
        output("Adam Driver now has" + newestStr)
    numberOfCredits = newestStr
    
    print(newestStr) #print text
    

    
if __name__ == "__main__":
    
    while not False:
        magic_happens()
        time.sleep(int(userDictionary["checkRate"]))
