import requests
import pycurl
import urllib2
import os
from bs4 import BeautifulSoup
from StringIO import StringIO


os.system('clear')


#open the file to dump the adres in
i=i+1
# specify the url
url ="https://www.google.com"
#url ="https://www.kinderdagverblijf-info.nl/" + line
print("Probing page: " + url)
quote_page = url
page = urllib2.urlopen(quote_page)
# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, "html.parser")
strSoup=str(soup)

print(strSoup)
