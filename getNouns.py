#do pip instal requests[security] to get around weird requests error
import nltk
from nltk.corpus import wordnet as wn
import requests
from PIL import Image
from StringIO import StringIO
import re

text = nltk.word_tokenize("candy apples are almost as delicious as fruit soda snakes.")
res = nltk.pos_tag(text)

goodWords = []
synsets = []
imagenetURL = "http://www.image-net.org/api/text/imagenet.synset.geturls.getmapping?wnid="
imageNetSettings = "&username=aferriss&accesskey=2673bac1a23ee6999056c857455ae60070303206&release=latest&src=stanford"
linkListsRaw = []
linkLists = []

for i, j in res:
	if j == 'NN' or j == 'NNS' or j == 'PRP' or j == 'FARTO' :
		word = wn.morphy(i)
		goodWords.append(word)

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

for word in goodWords:
	getImages(word, 0, 5)	

# for i in range(len(goodWords)):
# 	ss = wn.synset(goodWords[i]+'.n.01')
# 	wordNetID = ss.pos()+str(ss.offset()).zfill(8)
# 	print goodWords[i] + " " + wordNetID
# 	linkList = requests.get(imagenetURL+wordNetID+imageNetSettings).text
# 	if len(linkList) > 10:
# 		linkListsRaw.append(linkList)


# def getImage(url):
# 	r = requests.get(url)
# 	i = Image.open(StringIO(r.content))
# 	i.show()

# def extract_urls(your_text):
#   url_re = re.compile(r"(http://[^ ]+)")
#   # url_re = re.compile(r'\b(([\w-]+://?|www[.])[^\s()<>]+(?:\([\w\d]+\)|([^[:punct:]\s]|/)))')
#   for match in url_re.finditer(your_text):
#     yield match.group(0)

# for i in range(len(linkListsRaw)):
# 	linkListFormat = []
# 	for uri in extract_urls(linkListsRaw[i]):
# 		if(uri[0] != 'n'):
# 			linkListFormat.append(uri)
# 	linkLists.append(linkListFormat)

# goodUrls = []

# def checkUrl(urls):
# 	counter = 0
# 	for j in range(len(urls)):
# 		try:
# 			if counter < 10:
# 				r = requests.get(urls[j])
# 				if r.status_code == 200:
# 					i = Image.open(StringIO(r.content))
# 					i.show()
# 					goodUrls.append(urls[j])
# 					counter = counter+1
# 		except Exception, ex:
# 			#print ex
# 			print "fuck"


# for i in range(len(linkLists)):
# 	checkUrl(linkLists[i])


	
	





