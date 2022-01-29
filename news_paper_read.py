import pyttsx3
import requests
from pygame import mixer
import json
# initialisation
def speak(str):
       engine = pyttsx3.init()
       engine.say(str)
       engine.runAndWait()

def musiconloop(file):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()

if __name__ == '__main__':
       speak("Todays top headline..Lest begin")
       url="https://newsapi.org/v2/top-headlines?country=in&apiKey" \
           "=9cb205bb91e84d4691c28b0d744edfc3"

       news = requests.get(url).text
       news_dict = json.loads(news)
       print(news_dict["articles"])
       arts = news_dict['articles']
       for article in arts:
           print("\U0001F62A")
           print(article['title'])
           # musiconloop("News Bulletin.mp3")
           speak(article['title'])
           speak("Moving on to the next news....listen carefully")

# testing
