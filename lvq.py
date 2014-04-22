
def normalize(inp):
	old_min = min(inp)
	old_range = max(inp) - old_min
	new_min =-1.0
	new_range =2.0
	for i in xrange(len(inp)):
		inp[i]=new_min+(inp[i]-old_min)/old_range*new_range
	return inp
def prepairset():
	f1=open("1by9/list.txt","r")
	f2=open("1by9/doc.txt","r")
	feature=eval(f1.read())
	docfreq=eval(f2.read())
	f1.close()
	f2.close()
	i=0
	j=0
	inp=[]
	weight=[]
	T=[]
	for doc in docfreq:
		temp=[]
		for word in feature:
			if word in doc:
				temp.append(doc[word])
			else:
				temp.append(0)
		#temp=normalize(temp)
		if i%100==0:
			weight.append(temp)
			j=j+1
		inp.append(temp)
		T.append(j)
		i=i+1;
	return [inp,weight,T]		
def lvq(inp,weight,T,lr=0.1,epoch=10):
	while epoch>0:
		i=0
		for it in inp:
			if i%100==0:
				i=i+1
				continue;
			d=[]
			for w in weight:
				t=0.0
				for j in xrange(len(w)):
					t+=(it[j]-w[j])*(it[j]-w[j])
				d.append(t)
			winval=min(d)
			ind=0
			for val in d:
				if winval==val:
					break
				ind+=1
			winner=ind
			if T[i]==winner+1:
				for j in xrange(len(weight[winner])):
					weight[winner][j]+=lr*(it[j]-weight[winner][j])
			else:
				for j in xrange(len(weight[winner])):
					weight[winner][j]-=lr*(it[j]-weight[winner][j])	
			i=i+1
		lr=0.5*lr
		epoch-=1
		print("epoch "+str(10-epoch)+" completed")
	return weight
def main():
	[inp,weight,T]=prepairset()
	print(weight[0],weight[19])
	weight=lvq(inp,weight,T)
	print(weight[0],weight[19])
if __name__ == "__main__":
    main()
		
