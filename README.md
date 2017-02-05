#craigslist poetry

i was feeling particularly lonely while looking for rooms to rent on 
craigslist, and clicked over to missed connections to see if my soulmate 
was looking back for me. i was discouraged to learn that there were so 
many, because it meant that i'd probably never find that special 
someone. i scraped together some software to sift through craigslist 
missed connection ads using markov chains, and poetry started to fall 
out. i decided, like i imagine most people do at some point, to turn my 
sorriness into a zine.

[issue one](https://github.com/ardendaily/markov-connections/raw/master/zines/MissedConnections.pdf)(pdf, 61kB)

[issue two](https://github.com/ardendaily/markov-connections/raw/master/zines/MissedConnections2.pdf)(pdf, 62kB)

[issue three](https://github.com/ardendaily/markov-connections/raw/master/zines/MissedConnections3.pdf)(pdf, 62kB)

## tech involved

a quick-and-dirty series of hacks to collect heaps of data from craigslist missed connections. bash scripts run curl jobs which are piped into python scripts for processing. 

## software use
### new and improved! easy to use!

software provided at-will, with no warranty or guarantee, etc. everything here is pretty simple.  this guide assumes you are running a GNU/Linux variant. miiiiight work on OSX?

### PATH ONE - use demo datasets 

1. generate poetry!

    `$ python markovify data-samples/mc_data_0.txt`

### PATH TWO - download your own datasets!

1. install dependencies

    `$ sudo apt-get install python-pip` or similar for your distro

    `$ sudo pip install bs4`

2. gather links

    `bash automatic.sh`

3. generate poems!

    `python markovify.py mc_data_$(DATE -I).txt`
