from collections import OrderedDict
from cleaning import applyStemming
def frequency(words):			
	'''
		input : words=>List of words
		output : freq=>Dictionary containing frequency of each words
	'''
	freq={}
	for word in words:
		if word in freq:
			freq[word]+=1
		else:
			freq[word]=1
	#print('frequency list',freq)
	return freq

# find position of words
def position(parts,words):
	pos={}
	for word in words:
		loc=0
		for part in parts:
			part=applyStemming(part)
			if word in part:
				pos[word]=loc
				break
			else:
				loc=loc+1
			
	return pos
					
	
		
def compactness(parts,words):
	compact={}
	for word in words:
		compact[word]=0
		for part in parts:
			part=applyStemming(part)	
			if word in part:
				compact[word]+=1
				
	return compact


def getfrequency(bag,fr):
	freq={}
	for word in bag:
		freq[word]=0
	for f in fr:
		for word in f:
			freq[word]+=f[word]
	return freq

def getposition(bag,position):
	pos={}
	for word in bag:
		pos[word]=0
	for f in position:
		for word in f:
			if(pos[word]==0):
				pos[word]=f[word]
	return pos

def getcompactness(bag,compactness):
	compact={}
	for word in bag:
		compact[word]=0
	for f in compactness:
		for word in f:
			compact[word]+=f[word]
	return compact



