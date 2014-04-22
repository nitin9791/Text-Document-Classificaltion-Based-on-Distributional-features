from operator import itemgetter, attrgetter
import random
import sys
import os
import math
import deap

popsize=100
csize=500
maxiter=1000
crossover_rate = 0.7
mutation_rate = 0.05
counter=0;
def getFeatures(value):
	f1=open(value+"/features/frequency.txt","r")
	f2=open(value+"/features/position.txt","r")
	f3=open(value+"/features/compactness.txt","r")
	freq=eval(f1.read())
	pos=eval(f2.read())
	comp=eval(f3.read())
	f1.close()
	f2.close()
	f3.close()
	return [freq,pos,comp]
def assosiation(freq):
	features=[]
	for word in freq:
		features.append(word)
	features.sort()
	return features
def getList(nof):
	lis=[]
	for i in xrange(nof):
		lis.append(i)
def initialization(nof):
	population=[]
	for i in xrange(100):
		population.append(random.sample(range(nof),csize))
	return population

def calcfitness(freq,pos,comp,chromo,features):
	sum1=0.0
	sum2=0.0
	for i in xrange(csize):
		word=features[chromo[i]]
		sum1+=comp[word]
		sum2+=freq[word]
	#print(sum1,sum2)
	fitness=(0.8*sum1+0.2*sum2)/(sum1+sum2)
	#print(fitness)
	return fitness

def rankpop(freq,pos,comp,chromos,features):
	fitnessscores=[]
	for chromo in chromos:
		fitnessscores.append(calcfitness(freq,pos,comp,chromo,features))
	pairedpop=zip(chromos,fitnessscores)
	rankedpop=sorted(pairedpop,key = itemgetter(-1), reverse = True)
	return rankedpop

""" taking a ranked population selects two of the fittest members using roulette method"""
def selectFittest (fitnessScores, rankedChromos):
	while 1 == 1: # ensure that the chromosomes selected for breeding are have different indexes in the population
    		index1 = roulette (fitnessScores)
    		index2 = roulette (fitnessScores)
    		if index1 == index2:
      			continue
    		else:
      			break

  
	ch1 = rankedChromos[index1] # select  and return chromosomes for breeding 
	ch2 = rankedChromos[index2]
	return ch1, ch2

"""Fitness scores are fractions, their sum = 1. Fitter chromosomes have a larger fraction.  """
def roulette (fitnessScores):
	index = 0
	cumalativeFitness = 0.0
	r = random.random()
   	for i in range(len(fitnessScores)): # for each chromosome's fitness score
    		cumalativeFitness += fitnessScores[i] # add each chromosome's fitness score to cumalative fitness
		if cumalativeFitness > r: # in the event of cumalative fitness becoming greater than r, return index of that chromo
      			return i


def crossover (ch1, ch2):
  # at a random chiasma
	r = random.randint(0,csize)
  	return ch1[:r]+ch2[r:], ch2[:r]+ch1[r:]


def mutate (ch):
	mutatedCh = []
	for i in ch:
		if random.random() < mutation_rate:
      			if i == 1:
        			mutatedCh.append(0)
      			else:
        			mutatedCh.append(1)
    		else:
      			mutatedCh.append(i)
  #assert mutatedCh != ch
  	return mutatedCh
      
"""Using breed and mutate it generates two new chromos from the selected pair"""
def breed (ch1, ch2):
  	newCh1, newCh2 = [], []
  	if random.random() < crossover_rate: # rate dependent crossover of selected chromosomes
    		newCh1, newCh2 = crossover(ch1, ch2)
  	else:
    		newCh1, newCh2 = ch1, ch2
  	newnewCh1 = mutate (newCh1) # mutate crossovered chromos
  	newnewCh2 = mutate (newCh2)
  	return newnewCh1, newnewCh2

""" Taking a ranked population return a new population by breeding the ranked one"""
def iteratePop (rankedPop):
	fitnessScores = [ item[-1] for item in rankedPop ] # extract fitness scores from ranked population
	rankedChromos = [ item[0] for item in rankedPop ] # extract chromosomes from ranked population

	newpop = []
  	newpop.extend(rankedChromos[:popsize/15]) # known as elitism, conserve the best solutions to new population
  
  	while len(newpop) != popsize:
    		ch1, ch2 = [], []
    		ch1, ch2 = selectFittest (fitnessScores, rankedChromos) # select two of the fittest chromos
        
    		ch1, ch2 = breed (ch1, ch2) # breed them to create two new chromosomes 
    		newpop.append(ch1) # and append to new population
    		newpop.append(ch2)
  	return newpop
 
def putinfile(value,newfreq,newpos,newcomp,featurelist):
	f1=open(value+"/selectedfeatures/frequency.txt","w")
	f2=open(value+"/selectedfeatures/position.txt","w")
	f3=open(value+"/selectedfeatures/compactness.txt","w")
	f1.write(str(newfreq))
	f2.write(str(newpos))
	f3.write(str(newcomp))
	f1.close()
	f2.close()
	f3.close()
	f1=open(value+"/list.txt","w")
	f1.write(str(featurelist))
	f1.close()

def main():
	folder=["1by9","2by8","3by7","4by6","5by5","6by4"] 
	for value in folder:
		[freq,pos,comp]=getFeatures(value)
		features=assosiation(freq)
		nof=len(features)
		lis=getList(nof)
		population=initialization(nof)
		for i in xrange(maxiter):
			rpop=rankpop(freq,pos,comp,population,features)
			population=iteratePop(rpop)
			print(i)
		maxfit=0.0
		i=1
		ind=0
		for chromo in population:
			if(maxfit<calcfitness(freq,pos,comp,chromo,features)):
				ind =i
				maxfit=calcfitness(freq,pos,comp,chromo,features)
			i=i+1
		solution=population[ind-1]
		newfreq={}
		newpos={}
		newcomp={}
		featurelist=[]
		for i in solution:
			featurelist.append(features[i])
			newfreq[features[i]]=freq[features[i]]
			newpos[features[i]]=pos[features[i]]
			newcomp[features[i]]=comp[features[i]]
		featurelist=list(set(featurelist))
		putinfile(value,newfreq,newpos,newcomp,featurelist)
		print("iteration complete")
		print(len(solution),len(newfreq),ind)		
if __name__ == "__main__":
    main()


	

