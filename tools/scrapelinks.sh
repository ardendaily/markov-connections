#!/bin/bash
# 
# curl wrapper for mass CL mining

for PREFIX in portland losangeles denver boston newyork chicago seattle sfbay
do 
	for SUFFIX in 1 100 200 300 400
	do
		curl "http://$PREFIX.craigslist.org/search/mis?s=$SUFFIX" \
		-H 'DNT: 1' -H 'Accept-Encoding: gzip, deflate, sdch' \
		-H 'Accept-Language: en-US,en;q=0.8' \
		-H 'Upgrade-Insecure-Requests: 1' \
		-H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36' \
		-H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' \
		-H "Referer: http://$PREFIX.craigslist.org/search/mis" \
		-H 'Connection: keep-alive' \
		--compressed \
		--silent | grep data-id | ./craigslinks.py $PREFIX 
		sleep 0.1
	done
done
