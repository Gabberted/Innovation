# We will read a stream and convert it into a stream
# then we will print it 
# and do some stats

#import
import os
import urllib.request
import sys
import argparse
import pycurl
from bs4 import BeautifulSoup


#var declarations
strVersion = "0.0.1"
strUrl=""
boVerbose=0

#read commandLine
parser=argparse.ArgumentParser()
parser.add_argument('-u', '--url', dest ="url", help="Provide the url to read into a string", metavar="URL")
parser.add_argument('-v', '--verbose', default=0, dest ="verbose", help="Verbose output. Please note this will output the html code of any given url.")



#main function
os.system('clear')
print("Start System version: " + strVersion)
print("init ReadStream")

args = parser.parse_args()
if args.verbose:
	boVerbose=1

if args.url:
	try:

		

		strUrl=str(args.url)
		print("strUrl: " + strUrl)
		strUrl="www.google.com"
		print("strUrl: " + strUrl)
		x = urllib.request.urlopen(strUrl)
		print(x.read())

		print("The following arguments are provided :" + strUrl)
		strSite="www.google.com"
		quote_page = strUrl
        	#page = urllib.urlopen(strUrl)

		# parse the html using beautiful soup and store in variable `soup`
        	#soup = BeautifulSoup(page, "html.parser")

		#mystr = mybytes.decode("utf-8")
		#mystr=str(soup)
		#soup.close()

		if boVerbose==1: print(mystr)

		#now lets strip

	except valueError:
		print("args.url error" + valueError)  

print("End Program ! Bye !")



