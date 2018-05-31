import nltk
import random
from nltk import bigrams
from nltk import word_tokenize
from nltk import sent_tokenize
import re
from nltk.corpus import gutenberg
raw = gutenberg.raw("burgess-busterbrown.txt")
# print(raw)
# sentences = re.split(r'[.?!]\s*', raw)
sentences = sent_tokenize(raw)
# print(sentences)
length = len(sentences)
final = []
for i in range(2,length):
    second= sentences[i].rsplit(None, 1)[-1].lower()
    first = sentences[i].split(None, 1)[0].lower()
    secondword = second.replace('"',"")
    firstword = first.replace('"',"")
    first = firstword
    second =  secondword
    firstword = first.replace('.',"")
    secondword = second.replace('.',"")
    final.append(firstword)
    final.append(secondword)
bi = list(bigrams(final))
text = "i should do it He will play football he will do it himself there are some books"

newtext =  word_tokenize(text)
bigramtext = list(bigrams(newtext))
news = word_tokenize(raw)
for texts in bigramtext:
    if texts in bi:
        newtexts = text.replace(texts[0]+ ' '+texts[1],texts[0]+' . ' + texts[1])
        text = newtexts
sentences = re.split(r'[.?!]\s*', text)
print(sentences)
