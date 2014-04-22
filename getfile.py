# open file
import re
from getwords import *
from findfeature import *
from os import listdir
i=0
s=[]
s=["1by9","2by8","3by7","4by6","5by5","6by4"]
for i in xrange(6):
	documents=[]
	for k in xrange(20):
		for j in xrange((i+1)*100):
			fo=open(s[i]+"/training/class"+str(k+1)+"/"+str(j+1)+".txt",'r')
			string=fo.read()
			documents.append(string)
			fo.close()
	#documents=string.strip().split('\n')
	nod=len(documents)
	bag=[]
	print(nod)
	file1=s[i]+"/features/"
	counter=1
	loc=1
	fr=[]
	position=[]
	compactness=[]
	for doc in documents:
		'''words=getwords(doc)
		words.sort()
		freq=frequency(words)
		temp=file1+str(counter)+".txt"
		fo1=open(temp,'w')
		fo1.write(str(freq))
		fo1.close()
		splitter=re.compile('\\W*')
		doc1=splitter.split(doc)
		parts=makeparts(doc1)
		words=list(set(words))
		pos=position(parts,words)
		temp=file2+str(counter)+".txt"
		fo1=open(temp,'w')
		fo1.write(str(pos))
		fo1.close()
		splitter=re.compile('\\W*')
		doc1=splitter.split(doc)
		parts=makeparts(doc1)
		words=list(set(words))
		compact=compactness(parts,words)
		temp=file3+str(counter)+".txt"
		fo1=open(temp,'w')
		fo1.write(str(compact))
		fo1.close()
		bag=bag+words;
		counter=counter+1'''
		[ words,freq,pos,compact ]=getwords(doc,loc)
		fr.append(freq)
		position.append(pos)
		compactness.append(compact)
		words.sort()
		bag=bag+words
		counter+=1
		loc=loc+1
	print(len(bag))
	bag=list(set(bag))
	bag.sort()
	print(len(bag))
	fo=open(s[i]+"/doc.txt","w")
	fo.write(str(fr))
	fo.close()
	freq=getfrequency(bag,fr)
	fo=open(file1+"frequency.txt","w")
	fo.write(str(freq))
	fo.close()
	pos=getposition(bag,position)
	fo=open(file1+"position.txt","w")
	fo.write(str(pos))
	fo.close()
	compact=getcompactness(bag,compactness)
	fo=open(file1+"compactness.txt","w")
	fo.write(str(compact))
	fo.close()
	print("iteration complete")
	




