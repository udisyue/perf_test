#!/bin/bash
echo "System Performace Monitor 1.0 Start"

echo ""
echo "Monitor pid ..."
# pid=`pidof pidof /usr/bin/python /usr/bin/multimech-run redis_stress | sed 's/ /,/g'`
# pidstat -p ${pid} -l -u -r  1 1 | grep Average

echo ""
echo "Monitor sar ..."
sar -u -r -n DEV 1 1| grep Average | egrep -v "lo|eth1|eth2|eth3"

# echo ""
# echo "Monitor neterror ..."
# sar -n EDEV 1 1| grep Average | egrep -v "lo|eth1|eth2|eth3"

echo ""
echo "Monitor netstat ..."
netstat -n | awk '/^tcp/ {++state[$NF]} END {for(key in state) print key,state[key]}'

