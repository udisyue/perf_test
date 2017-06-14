#!/bin/bash

g++  $1.cpp -I.. ../libhiredis.a -o $1
