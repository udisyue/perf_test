#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import sys
reload(sys)
sys.path.append("../script/cache")
import json
import time

redis_vec = {}
redis_vec["0"] = "192.168.232.14:5233,192.168.232.14:5234,192.168.232.15:5233,192.168.232.15:5234,192.168.232.40:5233,192.168.232.40:5234,192.168.232.40:5235"
redis_vec["1"] = "192.168.110.103:5233,192.168.110.104:5233,192.168.110.119:5233,192.168.110.120:5233,10.39.135.17:5233,10.39.135.22:5233,10.39.136.17:5233,10.39.136.23:5233,192.168.110.111:5233,192.168.110.112:5233,192.168.110.127:5233,192.168.110.128:5233" 
redis_vec["2"] = "192.168.14.170:5233,192.168.14.170:5234,192.168.14.170:5235" 

def main(in_param):

    in_param_dict = {}
    try:
        if type(in_param) == str:
            in_param_dict = json.loads(in_param)
        else:
            in_param_dict = in_param
    except Exception as e:
        return None

    data = {}
    cmdValue = '../script/cache/bin/lruQueue %s' % ( 
                   redis_vec[in_param_dict["redis"]])
    value = os.popen(cmdValue).read()
    try: 
        data["lru_queue"] = json.loads(value)
    except Exception as e:
        data["lru_queue"] = ""

    return data
    
if __name__ == '__main__':
    try:
        # set param
        in_param = {}
        in_param["redis"] = "0"
        print "origin: ", type(in_param)
        in_param_json = json.dumps(in_param)
        print "dict 2 json: ", type(in_param_json)
        in_param_dict = json.loads(in_param_json)
        print "json 2 dict: ", type(in_param_dict)
        time1 = time.time()
        print main(in_param_json)
        time2 = time.time()
        print "use time : ", time2-time1
    except KeyboardInterrupt:
        pass
    except Exception as e:
        raise
