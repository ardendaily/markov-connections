#!/usr/bin/python

from pymarkovchain import MarkovChain
from sys import stdin, argv

mc = MarkovChain("./missedmarkov")
mc.generateDatabase( ''.join(stdin) )


if len(argv) > 1:
	for x in range(0,25):
		print mc.generateStringWithSeed(str(argv[1]))
else:
	for x in range(0,25):
		print mc.generateString()