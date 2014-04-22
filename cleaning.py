import re
import nltk
import math
from collections import OrderedDict
from nltk import PorterStemmer
from nltk.corpus import stopwords
from nltk import WordNetLemmatizer 

# for lemmatizing the words

def lemmatize(tokens): 
	# lemmatize words. try both noun and verb lemmatizations 
	lmtzr = WordNetLemmatizer() 
	for i in range(0,len(tokens)): 
		res = lmtzr.lemmatize(tokens[i]) 
		if res == tokens[i]: 
			tokens[i] = lmtzr.lemmatize(tokens[i], 'v') 
		else: 
			tokens[i] = res 
	return tokens

def removeStopWords(words):
	'''
		input : words=>List of words
		output : words=>List of words after removing stop words
	'''
	stop_words=stopwords.words('english')
	s=['home','mail','admin','contact','copright','rights','reserve','sitemap']
	stop_words+=s
	
	for a in stop_words:
		while a in words:
			words.remove(a)
	#print('after removing stop words',words)
	return words
def applyStemming(words):
	'''
		input: words=>List of words
		output: temp=>List of stemmed words
	'''
	temp=lemmatize(words)
	return temp

