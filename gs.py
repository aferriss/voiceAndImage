from bs4 import BeautifulSoup
import re
import urllib2
import os
from PIL import Image
from StringIO import StringIO
import requests

def get_soup(url,header):
  return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)))

image_type = "Action"
# you can change the query for the image  here  
query = "doggies"
query= query.split()
query='+'.join(query)
url="https://www.google.com/search?q="+query+"&safe=off&biw=1542&bih=788&source=Inms&tbm=isch&sa=X&ved=0ahUKEwjWg7mB-NLLAhVO2GMKHYpDDpEQ_AUIBigB"#+query

print url
header = {'User-Agent': 'Mozilla/5.0'} 
soup = get_soup(url,header)

images = [a['src'] for a in soup.find_all("img", {"src": re.compile("gstatic.com")})]
#print images
for img in images:
	print img
	r = requests.get(img)
	i = Image.open(StringIO(r.content))
	i.show()
