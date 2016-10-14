#craigslist poetry

a quick-and-dirty series of hacks to collect heaps of data from craigslist missed connections. bash scripts run curl jobs which are piped into python scripts for processing. 

##use

software provided at-will, with no warranty or guarantee, etc. everything here is pretty simple.  this guide assumes you are running a GNU/Linux variant. miiiiight work on OSX?

1. install dependencies. tools require curl.

    `pip install bs4`

    `pip install pymarkovchain`

    `apt-get install curl`

2. gather links

    `bash 0001.sh > ./craigslinks.txt`

3. gather posts from links

    `bash 0002.sh > ./craigsposts.txt`

4. generate some nonsense

    4a. non-directed output
    `cat ./craigsposts.txt | markovfromstdin.py`

    4b. seed with term
    `cat ./craigsposts.txt | markovfromstdin.py SEARCH-TERM`