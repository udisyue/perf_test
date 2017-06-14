#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import sys
reload(sys)
sys.path.append("./script/fromMysql")
from db import CDataBase, SQL_CFG
import json
import time

def main(in_param):
    in_param_dict = {}
    try:
        if type(in_param) == str:
            in_param_dict = json.loads(in_param)
        else:
            in_param_dict = in_param
    except Exception as e:
        return None

    mql_db = CDataBase(SQL_CFG["host"],SQL_CFG["user"],SQL_CFG["passwd"],SQL_CFG["database_report"])
    sql = "SELECT daily_date, FROM_UNIXTIME(daily_date, '%%Y-%%m-%%d'), ota_id, cached_ratio FROM ota_quality_daily_statistics WHERE FROM_UNIXTIME(daily_date, '%%Y-%%m-%%d') >= '%s' AND FROM_UNIXTIME(daily_date, '%%Y-%%m-%%d') <= '%s' ORDER BY daily_date, ota_id;" % (in_param_dict['begin_time'], in_param_dict['end_time'])
    print sql
    result = mql_db.GetAllList(sql)

    # 画表格
    if in_param_dict['show_type'] == "1":
        return result

    # 画图
    allday = []
    if len(result) >  0 and len(result[0]) >  0:
        last_day = result[0][0]
    ota_list = ["booking(1)", "ean(2)", "agoda(3)", "unknown(4)", "elong(5)", 
                "hana(6)", "gta(7)", "vetu(8)", "ctrip(9)", "dida(10)",
                "hotelbeds(11)", "dotw(12)", "eanpackage(13)", "fgt(14)", "agodapackage(15)",
                "roomorama(16)", "hotelspro(17)", "zyx(18)", "tourico(19)", "miki(20)",
                "travellanda(21)", "relux(22)", "methabook(23)", "haoqiao(24)"
               ]
    cur_day = 0
    ts = []
    days = []
    otas = []
    rates = []
    aday = {}
    for a in result:
        cur_day = int(a[0])
        if cur_day != last_day:
            last_day = cur_day
            aday["ts"] = ts;
            aday["days"] = days;
            aday["otas"] = otas;
            aday["rates"] = rates;
            allday.append(aday)
            ts = []
            days = []
            otas = []
            rates = []
            aday = {}
        ts.append(int(a[0]))    # 时间"%Y-%m-%d"
        days.append(a[1])     # 时间戳
        otas.append(int(a[2]))  # otaid
        # otas.append(ota_list[int(a[1])])
        rates.append(("%.2f" % float(a[3])))  # 缓存命中率
    if len(otas) > 0:
        aday["ts"] = ts;
        aday["days"] = days;
        aday["otas"] = otas;
        aday["rates"] = rates;
        allday.append(aday)
    return allday


if __name__ == "__main__":
    in_param = {}
    in_param["begin_time"] = "2016-09-24"
    in_param["end_time"] = "2016-09-26"
    in_param["show_type"] = "0"
    in_param_json = json.dumps(in_param)
    print main(in_param_json)
