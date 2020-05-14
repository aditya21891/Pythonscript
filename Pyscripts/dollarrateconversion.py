# this program is used to extract dollar to rupee conversion prices

from bs4 import BeautifulSoup
import urllib2
url="https://www.compareremit.com/todays-best-dollar-to-rupee-exchange-rate/"
page=urllib2.urlopen(url)
soup=BeautifulSoup(page,"html.parser")
cmpnyrates=soup.find(‘div’, attrs={‘class’: ‘container’})
print cmpnyrates
