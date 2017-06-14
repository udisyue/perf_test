#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import sys
reload(sys)
sys.path.append("../script/cache")
import json
import time

redis_vec = {}
redis_vec["1"] = "192.168.110.103:5233,192.168.110.104:5233,192.168.110.119:5233,192.168.110.120:5233,10.39.135.17:5233,10.39.135.22:5233,10.39.136.17:5233,10.39.136.23:5233,192.168.110.111:5233,192.168.110.112:5233,192.168.110.127:5233,192.168.110.128:5233" 
redis_vec["0"] = "192.168.232.14:5233,192.168.232.14:5234,192.168.232.15:5233,192.168.232.15:5234,192.168.232.40:5233,192.168.232.40:5234,192.168.232.40:5235"
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
    # sign=rid_0_oid_13_hid_324748_mobile_0_ver_3_ci_20160626_co_20160627_bc_0_cl_0_of_0_adult_num_2_child_num_0#
    cmdKey = '../script/cache/bin/detailKey %s %s %s %s %s %s %s %s %s %s %s' % ( in_param_dict["otaid"],
                                                   in_param_dict["hotel_id"],
                                                   in_param_dict["mobile"],
                                                   in_param_dict["ver"], 
                                                   in_param_dict["checkin"],
                                                   in_param_dict["checkout"],
                                                   in_param_dict["bc"],
                                                   in_param_dict["cl"],
                                                   in_param_dict["of"],
                                                   in_param_dict["adult_num"],
                                                   in_param_dict["children"])
    data = {}
    key = os.popen(cmdKey).read()
    if key != "":
        key = "d_%s" % key
  
    cmdValue = '../script/cache/bin/detailValue %s %s' % ( 
                    redis_vec[in_param_dict["redis"]], key)

    value = os.popen(cmdValue).read()
 
    data["key"] = key
    try:
        data["value"] = json.loads(value)
    except Exception as e:
        data["value"] = ""

    return data
    
if __name__ == '__main__':
    try:
        # set param
        in_param = {}
        in_param["redis"] = "0"
        in_param["mobile"] = "0" 
        in_param["ver"] = "2" 
        in_param["otaid"] = "2" 
        in_param["checkin"] = "20161212"
        in_param["checkout"] = "20161213"
        in_param["bc"] = "0"
        in_param["cl"] = "0"
        in_param["of"] = "0"
        in_param["adult_num"] = "2"
        in_param["children"] = "0#"
        in_param["hotel_id"] = "324748"
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
