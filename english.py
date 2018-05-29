import nltk
import random
from nltk.corpus import movie_reviews
from nltk import bigrams
from nltk import word_tokenize
from nltk import sent_tokenize
import re
f = open('english.txt')
raw = f.read()
text = "you and i should go to school i am fine how are you i am fine Tell me more about you you should keep going this one is very tough"
print(text)
newtext =  word_tokenize(text)
bigramtext = list(bigrams(newtext))
news = word_tokenize(raw)
bi = list(bigrams(news))
for texts in bigramtext:
    if texts in bi:
        newtexts = text.replace(texts[0]+ ' '+texts[1],texts[0]+' . ' + texts[1])
        text = newtexts
sentences = re.split(r'[.?!]\s*', text)
print(sentences)
