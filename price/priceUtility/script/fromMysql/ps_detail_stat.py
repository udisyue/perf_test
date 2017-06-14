#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import sys
reload(sys)
# sys.setdefaultencoding("utf-8")
# sys.path.append("./script/fromMysql")
from db import CDataBase, SQL_CFG_170
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

    mql_db = CDataBase(SQL_CFG_170["host"],SQL_CFG_170["user"],SQL_CFG_170["passwd"],SQL_CFG_170["database_price"], SQL_CFG_170["port"])
    # 全部渠道
    sql = ""
    if in_param_dict['show_type'] == "0":
        sql = """SELECT date,
'ALL',
SUM(count_query), SUM(count_total), SUM(sum_total),
if(SUM(sum_total)=0,0, SUM(sum_total_mapped) / SUM(sum_total)),
if(SUM(count_total)=0,0,SUM(count_total_mapped) / SUM(count_total)),
if(SUM(sum_total_mapped)=0,0,SUM(sum_select) / SUM(sum_total_mapped)),
if(SUM(count_ota)=0,0,SUM(count_ota_fc) / SUM(count_ota)),
if(SUM(count_query)=0,0,SUM(count_price_change_by1per) / SUM(count_query)),
if(SUM(count_query)=0,0,SUM(count_price_change) / SUM(count_query)),
if(SUM(count_query)=0,0,SUM(count_price_no2yes) / SUM(count_query)),
if(SUM(count_query)=0,0,SUM(count_price_yes2no) / SUM(count_query)),
if(SUM(count_query)=0,0,SUM(count_price_lower) / SUM(count_query)),
if(SUM(count_query)=0,0,SUM(count_price_higher) / SUM(count_query)),
if(SUM(count_query)=0,0,SUM(count_total) / SUM(count_query)),
if(SUM(count_query+count_crawler_query)=0,0,SUM(count_crawler_query) / SUM(count_query+count_crawler_query))
FROM price_detail_day
WHERE date >= '%s' AND date <= '%s'
GROUP BY date""" % (in_param_dict["begin_time"], in_param_dict["end_time"]);
    elif in_param_dict['show_type'] == "1":
        sql = """SELECT date,
CASE booking_channel
WHEN '2' THEN 'PC'
WHEN '16' THEN'APP'
WHEN '32' THEN 'H5'
END,
SUM(count_query), SUM(count_total), SUM(sum_total),
if(SUM(sum_total)=0,0, SUM(sum_total_mapped) / SUM(sum_total)),
if(SUM(count_total)=0,0,SUM(count_total_mapped) / SUM(count_total)),
if(SUM(sum_total_mapped)=0,0,SUM(sum_select) / SUM(sum_total_mapped)),
if(SUM(count_ota)=0,0,SUM(count_ota_fc) / SUM(count_ota)),
if(SUM(count_query)=0,0,SUM(count_price_change_by1per) / SUM(count_query)),
if(SUM(count_query)=0,0,SUM(count_price_change) / SUM(count_query)),
if(SUM(count_query)=0,0,SUM(count_price_no2yes) / SUM(count_query)),
if(SUM(count_query)=0,0,SUM(count_price_yes2no) / SUM(count_query)),
if(SUM(count_query)=0,0,SUM(count_price_lower) / SUM(count_query)),
if(SUM(count_query)=0,0,SUM(count_price_higher) / SUM(count_query)),
if(SUM(count_query)=0,0,SUM(count_total) / SUM(count_query)),
if(SUM(count_query+count_crawler_query)=0,0,SUM(count_crawler_query) / SUM(count_query+count_crawler_query))
FROM price_detail_day
WHERE date >= '%s' AND date <= '%s'
GROUP BY booking_channel,date
ORDER BY date, booking_channel""" % (in_param_dict["begin_time"], in_param_dict["end_time"]);
    elif in_param_dict['show_type'] == "2":
        sql = """SELECT date,
CASE booking_channel
WHEN '2' THEN 'PC'
WHEN '16' THEN'APP'
WHEN '32' THEN 'H5'
END,
SUM(count_query), SUM(count_total), SUM(sum_total),
if(SUM(sum_total)=0,0, SUM(sum_total_mapped) / SUM(sum_total)),
if(SUM(count_total)=0,0,SUM(count_total_mapped) / SUM(count_total)),
if(SUM(sum_total_mapped)=0,0,SUM(sum_select) / SUM(sum_total_mapped)),
if(SUM(count_ota)=0,0,SUM(count_ota_fc) / SUM(count_ota)),
if(SUM(count_query)=0,0,SUM(count_price_change_by1per) / SUM(count_query)),
if(SUM(count_query)=0,0,SUM(count_price_change) / SUM(count_query)),
if(SUM(count_query)=0,0,SUM(count_price_no2yes) / SUM(count_query)),
if(SUM(count_query)=0,0,SUM(count_price_yes2no) / SUM(count_query)),
if(SUM(count_query)=0,0,SUM(count_price_lower) / SUM(count_query)),
if(SUM(count_query)=0,0,SUM(count_price_higher) / SUM(count_query)),
if(SUM(count_query)=0,0,SUM(count_total) / SUM(count_query)),
if(SUM(count_query+count_crawler_query)=0,0,SUM(count_crawler_query) / SUM(count_query+count_crawler_query))
FROM price_detail_day
WHERE date >= '%s' AND date <= '%s'
AND booking_channel=2
GROUP BY date ORDER BY date""" % (in_param_dict["begin_time"], in_param_dict["end_time"])
    elif in_param_dict['show_type'] == "3":
        sql = """SELECT date,
CASE booking_channel
WHEN '2' THEN 'PC'
WHEN '16' THEN'APP'
WHEN '32' THEN 'H5'
END,
SUM(count_query), SUM(count_total), SUM(sum_total),
if(SUM(sum_total)=0,0, SUM(sum_total_mapped) / SUM(sum_total)),
if(SUM(count_total)=0,0,SUM(count_total_mapped) / SUM(count_total)), 
if(SUM(sum_total_mapped)=0,0,SUM(sum_select) / SUM(sum_total_mapped)),
if(SUM(count_ota)=0,0,SUM(count_ota_fc) / SUM(count_ota)),
if(SUM(count_query)=0,0,SUM(count_price_change_by1per) / SUM(count_query)),
if(SUM(count_query)=0,0,SUM(count_price_change) / SUM(count_query)),
if(SUM(count_query)=0,0,SUM(count_price_no2yes) / SUM(count_query)),
if(SUM(count_query)=0,0,SUM(count_price_yes2no) / SUM(count_query)),
if(SUM(count_query)=0,0,SUM(count_price_lower) / SUM(count_query)),
if(SUM(count_query)=0,0,SUM(count_price_higher) / SUM(count_query)),
if(SUM(count_query)=0,0,SUM(count_total) / SUM(count_query)),
if(SUM(count_query+count_crawler_query)=0,0,SUM(count_crawler_query) / SUM(count_query+count_crawler_query)) 
FROM price_detail_day
WHERE date >= '%s' AND date <= '%s'
AND booking_channel=16
GROUP BY date ORDER BY date""" % (in_param_dict["begin_time"], in_param_dict["end_time"])
    else:
        sql = """SELECT date,
CASE booking_channel
WHEN '2' THEN 'PC'
WHEN '16' THEN'APP'
WHEN '32' THEN 'H5'
END,
SUM(count_query), SUM(count_total), SUM(sum_total),
if(SUM(sum_total)=0,0, SUM(sum_total_mapped) / SUM(sum_total)),
if(SUM(count_total)=0,0,SUM(count_total_mapped) / SUM(count_total)), 
if(SUM(sum_total_mapped)=0,0,SUM(sum_select) / SUM(sum_total_mapped)),
if(SUM(count_ota)=0,0,SUM(count_ota_fc) / SUM(count_ota)),
if(SUM(count_query)=0,0,SUM(count_price_change_by1per) / SUM(count_query)),
if(SUM(count_query)=0,0,SUM(count_price_change) / SUM(count_query)),
if(SUM(count_query)=0,0,SUM(count_price_no2yes) / SUM(count_query)),
if(SUM(count_query)=0,0,SUM(count_price_yes2no) / SUM(count_query)),
if(SUM(count_query)=0,0,SUM(count_price_lower) / SUM(count_query)),
if(SUM(count_query)=0,0,SUM(count_price_higher) / SUM(count_query)),
if(SUM(count_query)=0,0,SUM(count_total) / SUM(count_query)),
if(SUM(count_query+count_crawler_query)=0,0,SUM(count_crawler_query) / SUM(count_query+count_crawler_query))
FROM price_detail_day
WHERE date >= '%s' AND date <= '%s'
AND booking_channel=32
GROUP BY date ORDER BY date""" % (in_param_dict["begin_time"], in_param_dict["end_time"])
    result = mql_db.GetAllList(sql)
    return result

if __name__ == "__main__":
    in_param = {}
    in_param["begin_time"] = "2017-04-28"
    in_param["end_time"] = "2017-05-02"
    in_param["show_type"] = "1"
    in_param_json = json.dumps(in_param)
    print main(in_param_json)
