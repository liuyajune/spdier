import requests
from urllib.parse import urlencode
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
from lxml import etree


baseurl = "http://job.tzrl.com/Search.aspx?"


# area=331002&key=&pageindex=2

def getOnePage(key, pageindex, area=331002):
    url = baseurl + urlencode({'area':area, 'key':key, 'pageindex':pageindex})
    print(url)
    html =  requests.get(url).text
    return html

url  = 'http://job.tzrl.com/Search.aspx?area=331002&key=&pageindex=2'

html = requests.get(url)
print(html.content)