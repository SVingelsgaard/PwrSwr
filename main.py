from bs4 import BeautifulSoup
import requests
import re

#testdata
url = ""
element = ""
headers = ""
cookies = ""

#main class
class scraper:
    def __init__(self, url, element, headers, cookies):
        self.url = url
        self.element = element
        self.headers = headers
        self.cookies = cookies

scraper(url, headers, cookies)