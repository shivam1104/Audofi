import urlparse2
import urllib
import urllib.request
import os
import numpy as Py
import sys
import re
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
'''
url = input('[+] Enter the URL: ')
download_path = input("[+] Enter the download path in full: ")
'''
url='http://freemusicarchive.org/genre/'
genre=['Country']


for genre_index in genre:
	Download_Page_url='http://freemusicarchive.org/genre/'+str(genre_index)+'/?page=1&per_page=100&sort=track_interest'
	print("Currently in Genre " + str(genre_index) + " Page = " +str(Download_Page_url))

	request = urllib.request.Request(Download_Page_url,headers={'User-Agent': 'Mozilla/5.0'})
	opener = urllib.request.build_opener()
	opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
	urllib.request.install_opener(opener)
	response = opener.open(request)
	data=response.read()
	text = data.decode('utf-8').encode('cp850','replace').decode('cp850')
	print(str(text))
	downloads=re.findall(r'https://freemusicarchive.org/music/download/*\w+\w?',text)
	print("Found "+str(len(downloads)) + " Songs")

	directory='../Songs/'+str(genre_index)+'/'
	if not os.path.exists(directory):
		os.makedirs(directory)

	counter=0
	for i in downloads:
		counter+=1
		if (counter>100):
			continue
		file_name='../Songs/'+str(genre_index)+'/'+str(counter)+'.mp3'
		print (file_name)	
		urllib.request.urlretrieve(i, file_name)

		print('Downloaded ' + str(counter))
		



print("Program Terminated")


'''
\w
<a href="https://freemusicarchive.org/music/download/
'''