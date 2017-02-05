#!/usr/bin/python
#
from bs4 import BeautifulSoup
from sys import stdin, argv

soupstring = "".join(stdin)
soup = BeautifulSoup(soupstring, "lxml")
results = soup.findAll("a")

for result in results:
	print "http://%s.craigslist.org%s" % (argv[1], result['href'])
