# We will read a stream and convert it into a stream
# then we will print it 
# and do some stats

#import
import os
import urllib.request


#var declarations
strVersion = "0.0.1"


#main
os.system('clear')
print("Start System version: " + strVersion)
print("init ReadStream")

fp = urllib.request.urlopen("http://www.python.org")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

print(mystr)


print("End Program ! Bye !")



