#!/usr/bin/python
from bs4 import BeautifulSoup
from sys import stdin

soupstring = "".join(stdin)
soup = BeautifulSoup(soupstring, "lxml")

try:
	title = soup.title.contents[0]
	body = soup.find("section", {"id":"postingbody"})
	content = body.getText().split("QR Code Link to This Post")[1]

	# might have to be xx.value
	print title
	print content
	print ""
	print ""
except:
	exit(0)
