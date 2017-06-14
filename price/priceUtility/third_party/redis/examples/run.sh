#!/bin/bash

g++  $1.cpp -I.. -I../../jsoncpp/include ../../jsoncpp/libs/linux-gcc-4.4.7/libjson_linux-gcc-4.4.7_libmt.a ../libhiredis_vip.a -o $1
