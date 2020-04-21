from bs4 import BeautifulSoup
import urllib2
import requests
import re
url_page = "https://www.theguardian.com/world/ng-interactive/2020/apr/08/coronavirus-map-of-the-us-latest-cases-state-by-state"
html_text = requests.get(url_page).text
soup = BeautifulSoup(html_text, 'html.parser')
rows = soup.findAll('tr', attrs={'class': re.compile('class1.*')})
print (rows)
# for link in soup.find_all('a'):
#     print(link.get('href'))
