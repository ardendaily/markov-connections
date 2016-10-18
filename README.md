#craigslist poetry

i was feeling particularly lonely while looking for rooms to rent on 
craigslist, and clicked over to missed connections to see if my soulmate 
was looking back for me. i was discouraged to learn that there were so 
many, because it meant that i'd probably never find that special 
someone. never to back away from a challenge, i scraped together some 
software to sift through craigslist missed connection ads using markov 
chains, and poetry started to fall out. i decided, like i imagine most 
people do at some point, to turn my sorriness into a zine.

[download the zine!](https://github.com/ardendaily/markov-connections/raw/master/MissedConnections.pdf)(pdf, 60.7k)


## tech involved

a quick-and-dirty series of hacks to collect heaps of data from craigslist missed connections. bash scripts run curl jobs which are piped into python scripts for processing. 

## software use

software provided at-will, with no warranty or guarantee, etc. everything here is pretty simple.  this guide assumes you are running a GNU/Linux variant. miiiiight work on OSX?

1. install dependencies. tools require curl.

    `pip install bs4`

    `pip install pymarkovchain`

    `apt-get install curl`

2. gather links

    `bash 0001.sh > ./craigslinks.txt`

3. gather posts from links

    `bash 0002.sh > ./craigsposts.txt`

4. generate some poetry

    4a. non-directed output
    `cat ./craigsposts.txt | markovfromstdin.py`

    4b. seed with term
    `cat ./craigsposts.txt | markovfromstdin.py SEARCH-TERM`
