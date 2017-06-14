#!/bin/bash

g++  $1.cpp -I.. ../libhiredis_vip.a -o $1
