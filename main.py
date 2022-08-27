from datetime import date
from time import time
from bs4 import BeautifulSoup
import requests
import re
from datetime import datetime
import webbrowser

#time. for the url

date = datetime.now().strftime("%d.%m.%y")
hour = datetime.now().strftime("%H")#10%3A58
min = datetime.now().strftime("%M")

print(date, min, hour)

#where and what to read
url = f"https://www.atb.no/reiseplanlegger/?direction=1&tplang=no&from=Ladeveien%20(Trondheim)&to=Buran%201%20(Trondheim)&Time={hour}%3A{min}&Date={date}&changepause=0&changepenalty=1"
#webbrowser.open(url)
element = "tm-main-inne"


#main class
class scraper:
    def __init__(self, url, element):
        self.url = url
        self.element = element
        self.doc = BeautifulSoup(requests.get(self.url).text, "html.parser")
        print(self.doc)

    def gatherData(self):
        self.data = self.doc.find(class_ = self.element)
        print(self.data)

scraper(url, element).gatherData()