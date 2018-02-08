import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
from lxml import etree


baseurl = "http://job.tzrl.com/Search.aspx?"


# area=331002&key=&pageindex=2

def getOnePage(key, pageindex,area=331002):
    url = baseurl + urlparse(area, key, pageindex)
    html =  requests.get(url).text
    return html


if __name__ == '__main__':
    print(getOnePage('',2))