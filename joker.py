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
		os.system("espeak 'Hello! this is Joker at your Service'")
		audio = r.listen(source) #source initialized to listen from microphone and load speech-to-text data

		try:
			string1 = r.recognize_google(audio) #allot recognized string to a Variable

			print(string1)
			switch(string1):
				case('hi' or 'hii' or 'hiii' or 'hello'):
					os.system("espeak 'Hello sir, what can I do for you'")

				case("what is the time" or "tell me time" or "time"):
					print(datetime.datetime.now())
					os.system("espeak 'Time! is ticking bro..!'")
		
				case("open Google"):
					os.system("espeak 'Opening Google!")
					webbrowser.open_new_tab(google_website)
	
				case("open YouTube" or "YouTube"):
					os.system("espeak 'Opening YouTube'")
					webbrowser.open_new_tab(youtube_website)

				case("open website"):
					new_website = input("Enter any valid website: ")
					os.system("espeak 'Enter any valid website'")
					webbrowser.open_new_tab(new_website)
		
		except:
			os.system("espeak 'Sorry could not recognize your voice'")

	
