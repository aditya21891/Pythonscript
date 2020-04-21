# This script is used to compare the prices currency conversion from various websites 
# author Aditya 

from urllib.request import urlopen as uReq
import re  
from bs4 import BeautifulSoup 
cnvrturl="https://www.compareremit.com/todays-best-dollar-to-rupee-exchange-rate/"
uclient=uReq(cnvrturl)
cnvrthtml=uclient.read()
soup=BeautifulSoup(uclient,"html.parser")
print (soup.get_text())
print (soup.prettify())

'''
for cmpny in crncysp.find_all('a'):
	print(cmpny.get('href'))

#print (crncysp.p)
'''
