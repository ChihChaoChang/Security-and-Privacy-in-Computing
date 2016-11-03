f = open('q5.txt')
count = 0		
array=[]
dict = {};
for wordLine in f:
	wordLine=wordLine.strip()
	if (wordLine.startswith("Internet Protocol Version 4, Src: ")):
		ip=wordLine.split()
		ip=wordLine[29:50]
	if (wordLine.startswith("Server")):
		wordLine=wordLine.split()
		array.append(wordLine[1])
		version=wordLine[1]
		if version not in dict:	
			dict[version]=[]
			dict[version].append(ip)
		count=count+1	
	
array.sort()

print "The the oldest version of Apache is "+array[0]
print "The IP address is: "
print dict[array[0]]

f.close()
