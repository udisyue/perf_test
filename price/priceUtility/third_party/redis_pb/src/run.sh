#!/bin/bash

g++  $1.cpp -I./third_party/include/redis ./third_party/lib/libhiredis_vip.a -o $1
