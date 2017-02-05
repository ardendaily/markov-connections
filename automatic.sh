#!/bin/bash
#
# this script runs all of the steps to download
# and scrape craiglist missed connections posts. 
# it will dump its results into a file.

finalfile="mc_data_$(date -I).txt"

echo "Starting. This may take some time."
cd tools

# scrape links from search results page
echo "Scraping links from search results page."
bash scrapelinks.sh >> .cl_temp

# dedup links
echo "Deduplicating links"
python removedupes.py .cl_temp >> .cl_temp_nodup

# scrape posts
echo "Downloading posts to $finalfile" 
echo "This may take a while."
bash downloadposts.sh >> $finalfile
mv $finalfile ../$finalfile

# clean up
echo "Cleaning up temp files."
rm .cl_temp .cl_temp_nodup

echo "Done!"