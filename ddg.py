# https://duckduckgo.com/i.js?q=Temple%20of%20the%20Golden%20Pavilion&s=50
import requests
import json
from PIL import Image
from StringIO import StringIO
import requests

verbose = True

def getImages(query, startNum, numToShow):
	payload = {'q': query, 's': str(startNum)}
	url = "https://duckduckgo.com/i.js"

	r = requests.get(url, payload)
	rawData = r.json()
	if verbose: print r.url

	counter = 0
	for i in range(len(rawData["results"])):
		if counter < numToShow:
			try:
				img = rawData["results"][i]["image"]
				r = requests.get(img)
				i = Image.open(StringIO(r.content))
				i.show()
				counter = counter + 1
			except Exception, ex:
				if verbose:
					print ex

getImages("cats and boots", 0, 5)