#!/bin/bash

#Scans multiple hsots in a target list using Shodan (requires an initialized Shodan API Key)

for host in $(cat target_list.txt)
do
    shodan host $host >> ~/Desktop/shodan_results.txt
    sleep 1
done
