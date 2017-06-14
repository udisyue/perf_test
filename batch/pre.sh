#!/bin/bash

d=`date +%Y%m%d`

if [ -f output/$d ];then
    echo "file already exist, delete."
    rm output/$d
fi

nohup python price_info.py 2>&1 1>output/$d &
