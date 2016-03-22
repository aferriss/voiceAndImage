import speech_recognition as sr
import nltk

def cb(src, audio):
	try:
		said = src.recognize_google(audio)
		text = nltk.word_tokenize(said)
		tagged = nltk.pos_tag(text)


		print (said)
		print (tagged)
		for i, j in tagged:
			if j == 'NN' or j == 'NNS' or j == 'PRP' or j == 'NNP' :
				print i
	except sr.UnknownValueError:
	    print("Google Speech Recognition could not understand audio")
	except sr.RequestError as e:
	    print("Could not request results from Google Speech Recognition service; {0}".format(e))

r = sr.Recognizer()
m = sr.Microphone()

with m as source:
	r.adjust_for_ambient_noise(source)

stop_listening = r.listen_in_background(m, cb)

import time
# for _ in range(50): time.sleep(0.1)
# stop_listening()
while True: time.sleep(0.001)


