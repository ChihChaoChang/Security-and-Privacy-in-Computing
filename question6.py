f = open('q6.txt')
count = 0		
dict = {}
for wordLine in f:
	dicionary = {}
	wordLine=wordLine.strip()
	if (wordLine.startswith("Internet Protocol Version")):
		line=wordLine.split()
		ip=line[5]
	if (wordLine.startswith("User Datagram Protocol")):
		wordLine=wordLine.split()
		srcPort=wordLine[5]
		destPort=wordLine[7:10]
		if ip not in dict:
			dict[ip]=[]
		if srcPort not in dict[ip]:
			dict[ip].append(srcPort)
	count=count+1	

for x in dict:
	print "source port: "+ x,dict[x]
		
f.seek(0)
dict2 = {}
for wordLine in f:
	wordLine=wordLine.strip()
	if (wordLine.startswith("Internet Protocol Version")):
		line=wordLine.split()
		ip=line[5]
	if (wordLine.startswith("User Datagram Protocol")):
		wordLine=wordLine.split()
		destPort=wordLine[9]
		if ip not in dict2:
			dict2[ip]=[]
		if destPort not in dict2[ip]:
			dict2[ip].append(destPort)
	count=count+1	

for x in dict2:
	print "destination Port: "+ x,dict2[x]
		
f.close()
