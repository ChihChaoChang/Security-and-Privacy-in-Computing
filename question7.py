f = open('q7.txt')
count = 0	
dict = {}
for wordLine in f:
	dicionary = {}
	wordLine=wordLine.strip()
	if (wordLine.startswith("Internet Protocol Version")):
		line=wordLine.split()
		#print line[4:6]
		src_ip=line[5]
		#print line[7:9]
		dest_ip=line[8]
		IP =src_ip+dest_ip
		#counter=1
		if IP not in dict:
			dict[IP]=[0]
		if IP in dict:
			dict[IP][0]=dict[IP][0]+1
		
	count=count+1	

#for x in dict:
#	print  x, dict[x]
for x in dict:
	if 	(dict[x] >=5):
		print x,dict[x]
	


f.close()
