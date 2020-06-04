#!/bin/bash

for host in $(cat target_list.txt)
do
    shodan host $host >> ~/Desktop/Projects/Neptune/shodan_results.txt
    sleep 1
done
