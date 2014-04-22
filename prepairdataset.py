import os
import shutil
i=100
s=["1by9","2by8","3by7","4by6","5by5","6by4"]
train="/training/class"
test="/testing/class"
for j in xrange(6):
	for k in xrange(20):
		for l in range(1000):
			try:
				if l<i:
					#f1=open("mydataset/class"+str(k+1)+"/"+str(l+1)+".txt","rb")
					#f2=open(s[j]+train+str(k+1)+"/"+str(l+1)+".txt","wb")
					#shutil.copyfile("mydataset/class"+str(k+1)+"/"+str(l+1)+".txt",f2)
					shutil.copyfile("mydataset/class"+str(k+1)+"/"+str(l+1)+".txt",s[j]+train+str(k+1)+"/"+str(l+1)+".txt")
				else:
					#f1=open("mydataset/class"+str(k+1)+"/"+str(l+1)+".txt","rb")
					#f2=open(s[j]+test+str(k+1)+"/"+str(l+1)+".txt","wb")
					#shutil.copyfile("mydataset/class"+str(k+1)+"/"+str(l+1)+".txt",f2)
					shutil.copyfile("mydataset/class"+str(k+1)+"/"+str(l+1)+".txt",s[j]+test+str(k+1)+"/"+str(l+1)+".txt")
			except IOError:
				print("continue")
		print(str(k+1)+"completed")
	print(s[j]+"completed")
	i=i+100

