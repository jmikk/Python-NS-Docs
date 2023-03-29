import requests
from bs4 import BeautifulSoup as BS
import lxml

USER = "descriptive user agent here"
password = "noneya"
pin = None

headers = {"User-Agent": USER, "X-Password": password, "X-Pin": pin}

data = {
    'nation': 'this is a nation',
    'region': 'this is a region',
    'c': 'rmbpost',
    'text': 'Is this thing on?',
    'mode': 'prepare',
}

url = "https://www.nationstates.net/cgi-bin/api.cgi"

r = requests.post(url, headers=headers, data=data)

try:
    pin2 = r.headers["X-pin"]
    # print(pin2)
except:
    print(r)
    print(r.headers)
    print("despair")
    exit()

headers2 = {"User-Agent": USER, "X-Password": password, "X-Pin": pin2}
token = BS(r.text, "xml").find("SUCCESS").text
# print(token)

data2 = {
    'nation': 'this is a nation',
    'region': 'this is a region',
    'c': 'rmbpost',
    'text': 'Is this thing on?',
    'mode': 'execute',
    'token': token
}

url = "https://www.nationstates.net/cgi-bin/api.cgi"
r = requests.post(url, headers=headers2, data=data2)
