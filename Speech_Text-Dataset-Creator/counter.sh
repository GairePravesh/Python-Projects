#!/bin/bash
echo "" 
seconds=10; date1=$((`date +%s` + $seconds)); 
while [ "$date1" -ge `date +%s` ]; do 
  #echo -ne "$(date -u --date @$(($date1 - `date +%s` )) +%H:%M:%S)\r"; 
  echo -ne "$(tput setaf 1)$(date -u --date @$(($date1 - `date +%s`)) +%H:%M:%S)\r $(tput sgr0)"
done
