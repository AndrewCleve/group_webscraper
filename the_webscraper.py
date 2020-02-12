import requests
from bs4 import BeautifulSoup

def magic_happens():
    url = "https://JasonCulley.github.io"
    response = requests.get(url)
    soup = BeautifulSoup(response.content,"html.parser")
    results = soup.find("h1")
    print(results.text)
if __name__ == "__main__":
    magic_happens()

