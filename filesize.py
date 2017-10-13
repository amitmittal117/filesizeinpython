import urllib
print "Entourage"
for i in range(1,3):
	myurl="http://s1.bia2m.in/Series/Entourage/s1/Entourage%20-%20S01%20E0"+str(i)+"%20(Bia2Movies).avi"
	f = urllib.urlopen(myurl)
	size= f.headers
	print size
	# # size= f.headers
	# size =int(size)/1024/1024
	# print str(i)+" : "+str(size)