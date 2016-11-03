f = open('q1.txt')
count = 0	
dict = {}
for wordLine in f:
	if wordLine.startswith(' '):
		line=wordLine.split()
		#print line[8:]
		info=line[9]
		#print line[3]
		src_ip=line[2]
		if src_ip not in dict:
			dict[src_ip]=[info]

	count=count+1	

for x in dict:
	print "source ip: "+ x,dict[x]	
	

f.close()
