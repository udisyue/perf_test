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

    mql_db = CDataBase(SQL_CFG["host"],SQL_CFG["user"],SQL_CFG["passwd"],SQL_CFG["database_price"])
    sql = "SELECT * FROM log_stat WHERE log_day >= '%s' AND log_day <= '%s' ORDER BY log_day;" % (
                in_param_dict["begin_time"], in_param_dict["end_time"])
    result = mql_db.GetAllList(sql)
    return result


if __name__ == "__main__":
    in_param = {}
    in_param["begin_time"] = "2016-09-20"
    in_param["end_time"] = "2016-09-22"
    in_param_json = json.dumps(in_param)
    print main(in_param_json)
