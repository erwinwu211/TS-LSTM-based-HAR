#!/bin/bash
DIR=$(dirname $(readlink -f $0))
cd $DIR
python Start.py
