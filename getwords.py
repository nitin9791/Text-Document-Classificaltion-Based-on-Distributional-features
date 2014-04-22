from cleaning import *
import re
import math
from findfeature import *
def getwords(doc,loc):
    splitter=re.compile('\\W*')
    # Split the words by non-alpha characters
    words=[s.lower( ) for s in splitter.split(doc)
           if len(s)>2 and len(s)<20 ]
    '''words=[]
    for s in word:
        if s in words:
            continue
        else:
            words.append(s) '''
    words=applyStemming(words) #apply stemming
    words=removeStopWords(words) # remove stop words
    freq=frequency(words)
    pos={}
    for word in words:
    	pos[word]=loc
    compact={}
    for word in words:
    	compact[word]=1
    return [words,freq,pos,compact]
