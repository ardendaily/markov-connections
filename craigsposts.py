#!/usr/bin/python
from bs4 import BeautifulSoup
from sys import stdin

soupstring = "".join(stdin)
soup = BeautifulSoup(soupstring, "lxml")

try:
	title = soup.title.contents[0]
	body = soup.find("section", {"id":"postingbody"}).contents[0]

	# might have to be xx.value
	print title
	print body
	print ""
	print ""
except:
	exit(0)