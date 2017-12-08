# coding: utf-8
import tkinter as tk
import re
import os
import wikipedia
import time
import webbrowser
import json
import requests
import ctypes
import random
from urllib.request import urlopen
import ssl
from bs4 import BeautifulSoup
import logging
#from urllib import urlopen
import speech_recognition as sr
import pyttsx3 as pyttsx
requests.packages.urllib3.disable_warnings()
try:
        _create_unverified_https_context=ssl._create_unverified_context
except 'AttributeError':
        pass
else:
        ssl._create_default_https_context=_create_unverified_https_context

headers = {'''user-agent':'Chrome/53.0.2785.143'''}
#speak=wicl.Dispatch("SAPI.SpVoice")

# Creating the graphical user interface
i=0
class MyFrame(tk.Frame):
        def __init__(self,*args,**kwargs):
            tk.Frame.__init__(self,*args,**kwargs)
            self.textBox = tk.Text(root,height=1,width=50)
            self.textBox.pack()
            root.bind('<Return>', self.OnEnter)
            self.textBox.focus_set()
            self.put=''
            self.audioInput=''
            self.say('''Hi Agent! BENJI at your service''')
            self.btn = tk.Button(root, text="Click to Speak",command=self.audio).pack()

        def say(self, arg):
            engine = pyttsx.init()
            engine.say(arg)
            engine.runAndWait()

        def audio(self):
            r = sr.Recognizer()
            print("Say something!")
            with sr.Microphone() as source:
                audio = r.listen(source)
            try:
                self.audioInput=r.recognize_google(audio)
            except sr.UnknownValueError:
                logging.info("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                logging.info("Could not request results from Google Speech Recognition service; {0}".format(e))

        def OnEnter(self,event=None):
            self.put=self.textBox.get("1.0","end-1c")
            print(self.put)
            link = self.put.split()
            print(link)
            #self.textBox.insert('0',"")
            identity_keywords = ["who are you", "who r u", "what is your name"]
            youtube_keywords = ["play", "stream", "queue"]
            launch_keywords = ["open", "launch"]
            search_keywords = ["search", "google"]
            wikipedia_keywords = ["wikipedia", "wiki"]

            if any(word in self.put for word in youtube_keywords):
                try:
                    link = '+'.join(link[1:])
#                    print(link)
                    say = link.replace('+', ' ')
                    url = 'https://www.youtube.com/results?search_query='+link
#                    webbrowser.open('https://www.youtube.com'+link)
                    fhand=urlopen(url).read()
                    soup = BeautifulSoup(fhand, "html.parser")
                    songs = soup.findAll('div', {'class': 'yt-lockup-video'})
                    hit = songs[0].find('a')['href']
#                    print(hit)
                    self.say("playing "+say)

                    webbrowser.open('https://www.youtube.com'+hit)
                except:
                    print('Sorry Ethan. Looks like its not working!')

            elif any(word in self.put for word in identity_keywords):
                try:
                    self.say("I am BENJI, a digital assistant declassified for civilian use. Previously I was used by the Impossible Missions Force")

                except:
                    print('Error. Try reading the ReadMe to know about me!')
        #Open a webpage
            elif any(word in self.put for word in launch_keywords):
                        try:
                            print(link[1])
                            self.say("opening "+link[1])
                            webbrowser.open('http://www.'+link[1]+'.com')
                        except:
                            print('Sorry Ethan,unable to access it. Cannot hack either-IMF protocol!')
                #Google search
            elif any(word in self.put for word in search_keywords):
                        try:
                            link='+'.join(link[1:])
                            say=link.replace('+',' ')
                            self.say("searching google for "+say)

                            webbrowser.open('https://www.google.com/search?q='+link)
                        except:
                            print('Nope, this is not working.')
                #Wikipedia
            elif any(word in self.put for word in wikipedia_keywords):
                        try:
                            link = '+'.join(link[1:])
                            say = link.replace('+', ' ')
                            wikisearch = wikipedia.page(say)
                            self.say("Opening wikipedia page for" + say)

                            webbrowser.open(wikisearch.url)
                        except:
                        	print('Wikipedia could not either find the article or your Third-world connection is unstable')
               #Lock the device
            elif self.put.startswith('secure '):
                try:
                    self.say("locking the device")
                    ctypes.windll.user32.LockWorkStation()
                except :
                    print('Cannot lock device')
            elif self.put.startswith('aljazeera '):
                try:
                    aljazeeraurl = ('https://newsapi.org/v1/articles?source=al-jazeera-english&sortBy=latest&apiKey=571863193daf421082a8666fe4b666f3')
                    newsresponce = requests.get(aljazeeraurl)
                    newsjson = newsresponce.json()
                    self.say('Our agents from Al-Jazeera report this')

                    print('  =====Al Jazeera===== \n')
                    i = 1
                    for item in newsjson['articles']:
                        print(str(i) + '. ' + item['title'] + '\n')
                        print(item['description'] + '\n')
                        i += 1
                except:
                    print('Qatari agents have refused to share this intel, Ethan')

            elif self.put.startswith('bbc '):
                try:
                    bbcurl = ('https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=571863193daf421082a8666fe4b666f3')
                    newsresponce = requests.get(bbcurl)
                    newsjson = newsresponce.json()
                    self.say('Our agents from BBC report this')

                    print('  =====BBC===== \n')
                    i = 1
                    for item in newsjson['articles']:
                        print(str(i) + '. ' + item['title'] + '\n')
                        print(item['description'] + '\n')
                        i += 1
                except:
                    print('MI6 is going crazy! Not allowing this!')
            elif self.put.startswith('cricket '):
                try:
                    cricketurl = ('https://newsapi.org/v1/articles?source=espn-cric-info&sortBy=latest&apiKey=571863193daf421082a8666fe4b666f3')
                    newsresponce = requests.get(cricketurl)
                    newsjson = newsresponce.json()
                    self.say('Our agents from ESPN Cricket report this')

                    print('  =====CRICKET NEWS===== \n')
                    i = 1
                    for item in newsjson['articles']:
                        print(str(i) + '. ' + item['title'] + '\n')
                        print(item['description'] + '\n')
                        i += 1
                except:
                    print('Connection not secure')
            elif self.put.startswith('hindus '):
                try:
                    hindusurl = ('https://newsapi.org/v1/articles?source=the-hindu&sortBy=latest&apiKey=571863193daf421082a8666fe4b666f3')
                    newsresponce = requests.get(hindusurl)
                    newsjson = newsresponce.json()
                    self.say('Our agents from Hindu News report this')

                    print('  =====HINDU NEWS===== \n')
                    i = 1
                    for item in newsjson['articles']:
                        print(str(i) + '. ' + item['title'] + '\n')
                        print(item['description'] + '\n')
                        i += 1
                except:
                    print('R&A W is blocking our reports, Ethan. Sorry! ')

            elif any(word in self.put for word in identity_keywords):
                try:
                    self.say("I am BENJI, a digital assistant declassified for civilian use. Previously I was used by the Impossible Missions Force")

                except:
                    print('Error. Try reading the ReadMe to know about me!')
                #Open a webpage
            elif any(word in self.put for word in launch_keywords):
                        try:
                            self.say("opening "+link[1])
                            print(link[1])
                            webbrowser.open('http://www.'+link[1]+'.com')
                        except:
                            print('Sorry Ethan,unable to access it. Cannot hack either-IMF protocol!')
                #Google search
            elif any(word in self.put for word in search_keywords):
                        try:
                            link='+'.join(link[1:])
                            say=link.replace('+',' ')
                            self.say("searching google for "+say)

                            webbrowser.open('https://www.google.com/search?q='+link)
                        except:
                            print('Nope, this is not working.')
                #Wikipedia
            elif any(word in self.put for word in wikipedia_keywords):
                        try:
                            link = '+'.join(link[1:])
                            say = link.replace('+', ' ')
                            wikisearch = wikipedia.page(say)
                            self.say("Opening wikipedia page for" + say)

                            webbrowser.open(wikisearch.url)
                        except:
                        	print('Wikipedia could not either find the article or your Third-world connection is unstable')
       #Lock the device
            elif self.put.startswith('secure '):
                try:
                        self.say("locking the device")

                        ctypes.windll.user32.LockWorkStation()
                except :
                        print('Cannot lock device')

        #News of various press agencies
            elif self.put.startswith('aljazeera '):
                try:
                    aljazeeraurl = ('https://newsapi.org/v1/articles?source=al-jazeera-english&sortBy=latest&apiKey=571863193daf421082a8666fe4b666f3')
                    newsresponce = requests.get(aljazeeraurl)
                    newsjson = newsresponce.json()
                    self.say('Our agents from Al-Jazeera report this')

                    print('  =====Al Jazeera===== \n')
                    i = 1
                    for item in newsjson['articles']:
                        print(str(i) + '. ' + item['title'] + '\n')
                        print(item['description'] + '\n')
                        i += 1
                except:
                    print('Qatari agents have refused to share this intel, Ethan')
            elif self.put.startswith('bbc '):
                try:
                    bbcurl = ('https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=571863193daf421082a8666fe4b666f3')
                    newsresponce = requests.get(bbcurl)
                    newsjson = newsresponce.json()
                    self.say('Our agents from BBC report this')

                    print('  =====BBC===== \n')
                    i = 1
                    for item in newsjson['articles']:
                        print(str(i) + '. ' + item['title'] + '\n')
                        print(item['description'] + '\n')
                        i += 1
                except:
                    print('MI6 is going crazy! Not allowing this!')
            elif self.put.startswith('cricket '):
                try:
                    cricketurl = ('https://newsapi.org/v1/articles?source=espn-cric-info&sortBy=latest&apiKey=571863193daf421082a8666fe4b666f3')
                    newsresponce = requests.get(cricketurl)
                    newsjson = newsresponce.json()
                    self.say('Our agents from ESPN Cricket report this')

                    print('  =====CRICKET NEWS===== \n')
                    i = 1
                    for item in newsjson['articles']:
                        print(str(i) + '. ' + item['title'] + '\n')
                        print(item['description'] + '\n')
                        i += 1
                except:
                    print('Connection not secure')
            elif self.put.startswith('hindus '):
                try:
                    hindusurl = ('https://newsapi.org/v1/articles?source=the-hindu&sortBy=latest&apiKey=571863193daf421082a8666fe4b666f3')
                    newsresponce = requests.get(hindusurl)
                    newsjson = newsresponce.json()
                    self.say('Our agents from Hindu News report this')

                    print('  =====HINDU NEWS===== \n')
                    i = 1
                    for item in newsjson['articles']:
                        print(str(i) + '. ' + item['title'] + '\n')
                        print(item['description'] + '\n')
                        i += 1
                except:
                    print('R&A W is blocking our reports, Ethan. Sorry! ')

'''            if put=='':
#                print("debug")
                m=sr.Recognizer()
                with sr.Microphone() as srm:
                    audio=m.listen(srm)
                try:
                    self.txt.SetValue("Listening...")
                    put=m.recognize_google(audio)
                    put=put.lower()
                    link=put.split()
                    self.txt.SetValue(put)
                except sr.UnknownValueError:
                    print("BENJI could not understand audio")
                except sr.RequestError as RE:
                    print("could not request results from IMF archives;{0}".format(RE))
                except:
                    print("Unknown error occurred, while taking speech input!")
'''

    #Trigger the GUI. Light the fuse!
if __name__=="__main__":
    root = tk.Tk()
    view = MyFrame(root)
    root.geometry('{}x{}'.format(400, 100))
    view.pack(side="top",fill="both",expand=False)
    root.mainloop()
