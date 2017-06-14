#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import sys
reload(sys)
sys.path.append("./script/fromMysql")
from db import CDataBase, SQL_CFG
import json

def main(in_param):
    in_param_dict = {}
    try:
        if type(in_param) == str:
            in_param_dict = json.loads(in_param)
        else:
            in_param_dict = in_param
    except Exception as e:
        return None

    mql_db = CDataBase(SQL_CFG["host"],SQL_CFG["user"],SQL_CFG["passwd"],SQL_CFG["database_report"], SQL_CFG["port"])
    # sql = "SELECT * FROM list_cache_price WHERE dateTime >= '%s' AND dateTime <= '%s' ORDER BY dateTime;" % (
    #             in_param_dict["begin_time"], in_param_dict["end_time"])
    sql = "SELECT DATE_FORMAT(FROM_UNIXTIME(daily_date), '%%Y-%%m-%%d'), \
avg_hasprice, hasprice_1, hasprice_2, hasprice_3, \
hasprice_4, hasprice_5, hasprice_6, hasprice_7, \
hasprice_8, hasprice_9, hasprice_10, hasprice_11,\
hasprice_12 FROM ps_listcache_daily \
WHERE DATE_FORMAT(FROM_UNIXTIME(daily_date), '%%Y-%%m-%%d') >= '%s' \
AND DATE_FORMAT(FROM_UNIXTIME(daily_date), '%%Y-%%m-%%d') <= '%s' \
ORDER BY DATE_FORMAT(FROM_UNIXTIME(daily_date), '%%Y-%%m-%%d');" % (in_param_dict["begin_time"], in_param_dict["end_time"]);
    result = mql_db.GetAllList(sql)
    return result

if __name__ == "__main__":
    in_param = {}
    in_param["begin_time"] = "2017-01-22"
    in_param["end_time"] = "2017-01-22"
    in_param_json = json.dumps(in_param)
    print main(in_param_json)
