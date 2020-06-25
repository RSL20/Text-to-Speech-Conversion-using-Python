# TEXT TO SPEECH

# import libraries
from newspaper import Article
import nltk
from gtts import gTTS
import os

# get the article
article = Article('https://hackernoon.com/future-of-python-language-bright-or-dull-uv41u3xwx')
article.download()
article.parse()
nltk.download('punkt')
article.nlp()

# store the text of article in variable mytext
mytext = article.text
print(mytext)

# convert text to speech
language = 'en' # english
myobj = gTTS(text = mytext, lang = language, slow = False)

# save the converted audio to a file
myobj.save('read_article.mp3')

# play the converted file
os.system('start read_article.mp3')