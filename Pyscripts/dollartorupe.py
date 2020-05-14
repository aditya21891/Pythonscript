import requests
import urllib.request
import time
from bs4 import BeautifulSoup
url ="https://www.compareremit.com/todays-best-dollar-to-rupee-exchange-rate/"
response = requests.get(url)
soup = BeautifulSoup(response.text, “html.parser”)
