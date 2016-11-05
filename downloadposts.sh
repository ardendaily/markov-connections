#!/bin/bash
IFMODTIME=$(date +"%a, %d %b %Y %T %Z")
for LINK in $(cat craigslinks.txt | tr "\n" " ")
do
	curl --silent $LINK \
	-H 'DNT: 1' \
	-H 'Accept-Encoding: gzip, deflate, sdch' \
	-H 'Accept-Language: en-US,en;q=0.8' \
	-H 'Upgrade-Insecure-Requests: 1' \
	-H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36' \
	-H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' \
	-H 'Cache-Control: max-age=0' \
	-H 'Connection: keep-alive' \
	-H 'If-Modified-Since: $IFMODTIME' \
	--compressed | ./craigsposts.py >> missedconnections.txt
	sleep 0.1
done
