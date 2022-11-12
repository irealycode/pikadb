#!/bin/bash

pip3 install -r requierments.txt
mkdir ~/.dbs/
mkdir ~/.pikadb/
cp ./pikadb.py ~/.pikadb/
echo "python3 ~/.pikadb/pikadb.py" > /bin/pikadb
