#Sparky's JoKeR

import speech_recognition as sr #importing package for speech recognition
import datetime #for current date and time 	
import webbrowser #to communicate with your system's default browser
import os #espeak text-to-speech
google_website = "https://www.google.com" #creating a website shortcut or assigning value to it
youtube_website = "https://www.youtube.com" 

while True:	
	r= sr.Recognizer() #initializing speech recognizer
	with sr.Microphone() as source: #using microphone as a source
		print("Speak Anything: ") #initializing "JoKeR"
		audio = r.listen(source) #source initialized to listen from microphone and load speech-to-text data

		try:
			string1 = r.recognize_google(audio)
			print(string1)
		except:
			os.system("espeak 'Sorry could not recognize your voice'")

		if string1=="hi" or string1=="hii" or string1=="hiii" or string1=="hello":
			os.system("espeak 'Hello sir, what can I do for you'")

		elif string1=="what is the time" or string1=="tell me time" or string1=="time":
			print(datetime.datetime.now())

		elif string1=="open Google":
			os.system("espeak 'Opening Google'")
			webbrowser.open_new_tab(google_website)

		elif string1=="open YouTube" or string1=="YouTube":
			os.system("espeak 'Opening YouTube'")
			webbrowser.open_new_tab(youtube_website)

		elif string1=="open website":
			new_website = input("Enter any valid website: ")
			os.system("espeak 'Enter any valid website'")
			webbrowser.open_new_tab(new_website)
		
		
