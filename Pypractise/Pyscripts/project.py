from pytz import timezone
import pytz
import webbrowser
import urllib
from flask import Flask

from datetime import datetime
from time import strftime
print(strftime("%H:%M:%S"))
new=1;
videourl="https://www.youtube.com/playlist?list=PLzpeeMx5u9u3kvpmO2M8LaueQZT0PKq4M"
webbrowser.get('safari').open_new(videourl)
blog=1
burl="https://medium.com/topic/technology"
webbrowser.open_new_tab(burl)

temp=1;
turl="https://www.accuweather.com/en/us/"
