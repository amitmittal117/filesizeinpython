# import bs4
# import re
# from urllib import urlopen as uReq
# from bs4 import BeautifulSoup as soup
# from openpyxl import Workbook
# book = Workbook()
# sheet = book.active

# my_url = 'http://s1.bia2m.in/Series/Entourage'
# uClient = uReq(my_url)
# page_html = uClient.read()
# uClient.close()
# page_soup = soup(page_html, "html.parser")
# containers_season_div = page_soup.findAll("td")
# print containers_season_div
# # for i in range(7,15):
# # 	print i
# # 	print containers_season_div[i].string

import bs4 as bs
import urllib
import urllib2
from openpyxl import Workbook

book = Workbook()
sheet = book.active
count = count1 = 0
sname = "Entourage" # Exact name of season
lastseason = 5 # Last season number
lastseason = lastseason +1
for snumber in range(1,lastseason):
	count=count+1
	no = "s"+str(snumber)
	surl = "http://s1.bia2m.in/Series/"+sname+"/"+no+"/"
	sauce = urllib.urlopen(surl).read()
	soup = bs.BeautifulSoup(sauce,'lxml')
	for url in soup.find_all('a'):
		if '.avi' in surl+url.get('href'):
			count1 = count1 +1
			size = urllib.urlopen(surl+url.get('href')).headers["Content-Length"]
			size =int(size)/1024/1024
			print(surl+url.get('href'))+" size: "+str(size)+"M"
			# sheetpos = 'A' + str(count1)
			# sheet[sheetpos] = surl+url.get('href')
			# bookname = sname+".xlsx"
			# book.save(bookname)