#! /bin/bash
while read line ; do
    python grep.py $line
done
