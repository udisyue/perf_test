# !/usr/bin/python
# coding:utf-8

import sys
sys.path.append("../script/unitTest")
sys.path.append("../script/cache")
sys.path.append("../script/fromMysql")
from flask import Flask, request, render_template, url_for, jsonify
import json
import types
from common import server_ip, server_port, redis_index
import ps_list, ps_detail, ps_booking, ps_update
import ps_list_cache, ps_detail_cache
import ps_price_change_stat, ps_cache_stat, ps_list_cache_price
import ps_detail_stat
import ps_lru_stat
import sug_test
import time
import datetime

app = Flask(__name__)
app.config.from_object('config')
 
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html");

@app.route('/test')
def test():
    return render_template("test.html");

@app.route('/list', methods=['GET', 'POST'])
def list():
    if request.method == "POST":
        ip = request.values.get("IP")
        port = request.values.get("Port")
        show_type = request.values.get("showType")
        booking_channel = request.values.get("bookingChannel")
        # order_from = request.values.get("orderFrom")
        # customer_level = request.values.get("customerLevel")
        # user_ip = request.values.get("userIp")
        user_id = request.values.get("userId")
        activity_id = request.values.get("activityId")
        hotel_id = request.values.get("hotelId")
        region_id = request.values.get("regionId")
        filter_ota = request.values.get("filterOta")
        checkin = request.values.get("checkIn")
        checkout = request.values.get("checkOut")
        adult_num = request.values.get("audultNum")
        children = request.values.get("childAges")
        list_query_flag = request.values.get("listQueryFlag")
        search_id = request.values.get("searchId")
        in_param = {"ip": ip,
                "port": port,
                "show_type": show_type,
                "booking_channel": booking_channel,
                "user_id": user_id,
                "activity_id": activity_id,
                "hotel_id": hotel_id,
                "region_id": region_id,
                "filter_ota": filter_ota,
                "checkin": checkin,
                "checkout": checkout,
                "adult_num": adult_num,
                "children": children,
                "list_query_flag": list_query_flag,
                "search_id": search_id
        }
        out_param = ps_list.main(json.dumps(in_param))
        # return json.dumps(out_param)
        return render_template("list.html", req=in_param, result=out_param)
    else:
        # default param
        in_param = {"ip": server_ip,
                "port": "6300",
                "show_type":"0",
                "booking_channel": "2",
                "user_id": "",
                "activity_id": "",
                "hotel_id": "326482,324763,326777,324749,324650,324751,324752",
                "region_id": "0",
                "filter_ota": "455016366",
                "checkin": "2017-12-12",
                "checkout": "2017-12-13",
                "adult_num": "2",
                "children": "",
                "list_query_flag": "7",
                "search_id": "123456789"
        }
        return render_template("list.html", req=in_param, result=None)

@app.route('/detail', methods=['GET', 'POST'])
def detail():
    if request.method == "POST":
        ip = request.values.get("IP")
        port = request.values.get("Port")
        show_type = request.values.get("showType")
        booking_channel = request.values.get("bookingChannel")
        order_from = request.values.get("orderFrom")
        customer_level = request.values.get("customerLevel")
        # user_ip = request.values.get("userIp")
        user_id = request.values.get("userId")
        activity_id = request.values.get("activityId")
        hotel_id = request.values.get("hotelId")
        filter_ota = request.values.get("filterOta")
        checkin = request.values.get("checkIn")
        checkout = request.values.get("checkOut")
        adult_num = request.values.get("audultNum")
        children = request.values.get("childAges")
        search_id = request.values.get("searchId")
        selection = request.values.get("selection")
        request_type = request.values.get("requestType")
        in_param = {"ip": ip,
                "port": port,
                "show_type": show_type,
                "booking_channel": booking_channel,
                "order_from": order_from,
                "customer_level": customer_level,
                "user_id": user_id,
                "activity_id": activity_id,
                "hotel_id": hotel_id,
                "filter_ota": filter_ota,
                "checkin": checkin,
                "checkout": checkout,
                "adult_num": adult_num,
                "children": children,
                "search_id": search_id,
                "selection": selection,
                "request_type": request_type,
         }
        out_param = ps_detail.main(json.dumps(in_param))
        return render_template("detail.html", req=in_param, result=out_param)
    else:
        # default param
        in_param = {"ip": server_ip,
                "port": "6300",
                "show_type": "0",
                "booking_channel": "2",
                "order_from": "50",
                "customer_level": "1",
                "user_id": "",
                "activity_id": "2017000057",
                "hotel_id": "326482",
                "filter_ota": "455016366",
                "checkin": "2017-12-12",
                "checkout": "2017-12-13",
                "adult_num": "2",
                "children": "",
                "search_id": "123456789",
                "selection": "1",
                "request_type": "1",
        }
        return render_template("detail.html", req=in_param, result=None)

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == "POST":
        ip = request.values.get("IP")
        port = request.values.get("Port")
        show_type = request.values.get("showType")
        booking_channel = request.values.get("bookingChannel")
        order_from = request.values.get("orderFrom")
        customer_level = request.values.get("customerLevel")
        # user_ip = request.values.get("userIp")
        user_id = request.values.get("userId")
        hotel_id = request.values.get("hotelId")
        otaid = request.values.get("otaId")
        src_otaid = request.values.get("srcOtaId")
        checkin = request.values.get("checkIn")
        checkout = request.values.get("checkOut")
        adult_num = request.values.get("audultNum")
        children = request.values.get("childAges")
        elong_pid = request.values.get("elongPid")
        ota_sign = request.values.get("otaSign")
        search_id = request.values.get("searchId")
        room_num = request.values.get("roomNum")
        elong_pname = request.values.get("elongPname")
        in_param = {"ip": ip,
                "port": port,
                "show_type": show_type,
                "booking_channel": booking_channel,
                "order_from": order_from,
                "customer_level": customer_level,
                "user_id": user_id,
                "hotel_id": hotel_id,
                "src_otaid": src_otaid,
                "otaid": otaid,
                "checkin": checkin,
                "checkout": checkout,
                "adult_num": adult_num,
                "children": children,
                "elong_pid": elong_pid,
                "ota_sign": ota_sign,
                "search_id":search_id,
                "room_num":room_num,
                "elong_pname":elong_pname
        }
        out_param = ps_booking.main(json.dumps(in_param))
        return render_template("booking.html", req=in_param, result=out_param)
    else:
        in_param = {"ip": server_ip,
                "port": "6300",
                "show_type": "0",
                "booking_channel": "2",
                "order_from": "50",
                "customer_level": "1",
                "user_id": "",
                "hotel_id": "326482",
                "otaid": "2",
                "src_otaid": "-1",
                "checkin": "2017-12-12",
                "checkout": "2017-12-13",
                "adult_num": "2",
                "children": "",
                "elong_pid": "-4186676727831952919",
                "ota_sign": "-5818353521585934887",
                "search_id": "123456789",
                "room_num": "1",
                "elong_pname": "0"
        }
        return render_template("booking.html", req=in_param, result=None)

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == "POST":
        ip = request.values.get("IP")
        port = request.values.get("Port")
        booking_channel = request.values.get("bookingChannel")
        hotel_id = request.values.get("hotelId")
        otaid = request.values.get("otaId")
        checkin = request.values.get("checkIn")
        checkout = request.values.get("checkOut")
        adult_num = request.values.get("audultNum")
        children = request.values.get("childAges")
        search_id = request.values.get("searchId")
        list_only= request.values.get("listOnly")
        hotel_status= request.values.get("hotelStatus")
        # room1
        room1= request.values.get("room1")
        roomId1= request.values.get("roomId1")
        roomNameCn1= request.values.get("roomNameCn1")
        roomStatus1= request.values.get("roomStatus1")
        product11= request.values.get("product11")
        elongPid11= request.values.get("elongPid11")
        productNameCn11= request.values.get("productNameCn11")
        mobile11= request.values.get("mobile11")
        cashPay11= request.values.get("cashPay11")
        averRoomPrice11= request.values.get("averRoomPrice11")
        averPrice11= request.values.get("averPrice11")
        product12= request.values.get("product12")
        elongPid12= request.values.get("elongPid12")
        productNameCn12= request.values.get("productNameCn12")
        cashPay12= request.values.get("cashPay12")
        mobile12= request.values.get("mobile12")
        averRoomPrice12= request.values.get("averRoomPrice12")
        averPrice12= request.values.get("averPrice12")
        # room2
        room2= request.values.get("room2")
        roomId2= request.values.get("roomId2")
        roomNameCn2= request.values.get("roomNameCn2")
        roomStatus2= request.values.get("roomStatus2")
        product21= request.values.get("product21")
        elongPid21= request.values.get("elongPid21")
        productNameCn21= request.values.get("productNameCn21")
        cashPay21= request.values.get("cashPay21")
        mobile21= request.values.get("mobile21")
        averRoomPrice21= request.values.get("averRoomPrice21")
        averPrice21= request.values.get("averPrice21")
        product22= request.values.get("product22")
        elongPid22= request.values.get("elongPid22")
        productNameCn22= request.values.get("productNameCn22")
        cashPay22= request.values.get("cashPay22")
        mobile22= request.values.get("mobile22")
        averRoomPrice22= request.values.get("averRoomPrice22")
        averPrice22= request.values.get("averPrice22")
        data = {"ip": ip,
                "port": port,
                "booking_channel": booking_channel,
                "hotel_id": hotel_id,
                "otaid": otaid,
                "checkin": checkin,
                "checkout": checkout,
                "adult_num": adult_num,
                "children": children,
                "search_id": search_id,
                "list_only": list_only,
                "hotel_status": hotel_status,
                "room1": room1,
                "roomId1": roomId1,
                "roomNameCn1": roomNameCn1,
                "roomStatus1": roomStatus1,
                "product11": product11,
                "elongPid11": elongPid11,
                "productNameCn11": productNameCn11,
                "mobile11": mobile11,
                "cashPay11": cashPay11,
                "averRoomPrice11": averRoomPrice11,
                "averPrice11": averPrice11,
                "product12": product12,
                "elongPid12": elongPid12,
                "productNameCn12": productNameCn12,
                "cashPay12": cashPay12,
                "mobile12": mobile12,
                "averRoomPrice12": averRoomPrice12,
                "averPrice12": averPrice12,
                "room2": room2,
                "roomId2": roomId2,
                "roomNameCn2": roomNameCn2,
                "roomStatus2": roomStatus2,
                "product21": product21,
                "elongPid21": elongPid21,
                "productNameCn21": productNameCn21,
                "cashPay21": cashPay21,
                "mobile21": mobile21,
                "averRoomPrice21": averRoomPrice21,
                "averPrice21": averPrice21,
                "product22": product22,
                "elongPid22": elongPid22,
                "productNameCn22": productNameCn22,
                "cashPay22": cashPay22,
                "mobile22": mobile22,
                "averRoomPrice22": averRoomPrice22,
                "averPrice22": averPrice22
        }
        in_param = json.dumps(data)
        # return in_param
        out_param = ps_update.main(in_param)
        return render_template("update.html", result=out_param)
    else:
        return render_template("update.html", result=None)

@app.route('/list_cache', methods=['GET', 'POST'])
def list_cache():
    if request.method == "POST":
        redis = request.values.get("redis")
        ver = request.values.get("version")
        hotel_id = request.values.get("hotelId")
        adult_num = request.values.get("audultNum")
        # bc = request.values.get("bookingChannel")
        # cl = request.values.get("customerLevel")
        # of = request.values.get("orderFrom")
        children = request.values.get("childAges")
        checkin = request.values.get("checkIn")
        checkout = request.values.get("checkOut")
        in_param = {"ver": ver,
                "redis": redis,
                "checkin": checkin,
                "checkout": checkout,
                "hotel_id": hotel_id,
                "bc": "0",
                "cl": "0",
                "of": "0",
                "adult_num": adult_num,
                "children": children
        }
        out_param = ps_list_cache.main(json.dumps(in_param))
        return render_template("list_cache.html", req = in_param, result = out_param)
    else:
        # default param
        in_param = {"redis": redis_index,
                    "ver": "3",
                    "hotel_id": "326482",
                    "checkin": "20171212",
                    "checkout": "20171213",
                    "adult_num": "2",
                    "bc": "0",
                    "cl": "0",
                    "of": "0",
                    "children": "0#"}

        return render_template("list_cache.html", req = in_param, result=None)

@app.route('/detail_cache', methods=['GET', 'POST'])
def detail_cache():
    if request.method == "POST":
        redis = request.values.get("redis")
        ver = request.values.get("version")
        hotel_id = request.values.get("hotelId")
        adult_num = request.values.get("audultNum")
        # bc = request.values.get("bookingChannel")
        # cl = request.values.get("customerLevel")
        # of = request.values.get("orderFrom")
        children = request.values.get("childAges")
        checkin = request.values.get("checkIn")
        checkout = request.values.get("checkOut")
        otaid = request.values.get("otaId")
        mobile = request.values.get("mobile")
        in_param = {"ver": ver,
                "redis": redis,
                "checkin": checkin,
                "checkout": checkout,
                "hotel_id": hotel_id,
                "bc": "0",
                "cl": "0",
                "of": "0",
                "adult_num": adult_num,
                "children": children,
                "otaid": otaid,
                "mobile": mobile
        }
        out_param = ps_detail_cache.main(json.dumps(in_param))
        # return json.dumps(out_param)
        return render_template("detail_cache.html", req=in_param, result=out_param)
    else:
        # default param
        in_param = {"ver": "3",
                "redis": redis_index,
                "checkin": "20171212",
                "checkout": "20171213",
                "hotel_id": "326482",
                "bc": "0",
                "cl": "0",
                "of": "0",
                "adult_num": "2",
                "children": "0#",
                "otaid": "2",
                "mobile": "0"
        }
        return render_template("detail_cache.html", req=in_param, result=None)

@app.route('/lru_stat', methods=['GET', 'POST'])
def lru_stat():
    if request.method == "POST":
        redis = request.values.get("redis")
        in_param = {
            "redis": redis
        }
        out_param = ps_lru_stat.main(json.dumps(in_param))
        # return json.dumps(out_param)
        return render_template("lru_stat.html", req=in_param, result=out_param)
    else:
        in_param = {
            "redis": redis_index
        }
        return render_template("lru_stat.html", req=in_param, result=None)

@app.route('/cache_stat', methods=['GET', 'POST'])
def cache_stat():
    if request.method == "POST":
        begin_time = request.values.get("beginTime")
        end_time = request.values.get("endTime")
        show_type = request.values.get("showType")
        in_param = {"begin_time": begin_time,
                    "end_time": end_time,
                    "show_type": show_type
        }
        out_param = ps_cache_stat.main(json.dumps(in_param))
        # return json.dumps(out_param)
        if show_type == "0":
            return render_template("cache_stat.html", req=in_param, picture=out_param, result=None)
        else:
            return render_template("cache_stat.html", req=in_param, picture=None, result=out_param)
    else:
        in_param = {"begin_time": "2016-09-20",
                    "end_time": "2016-09-23",
                    "show_type": "0"
                   }
        return render_template("cache_stat.html", req=in_param, result=None)

@app.route('/list_cache_price', methods=['GET', 'POST'])
def list_cache_price():
    if request.method == "POST":
        begin_time = request.values.get("beginTime")
        end_time = request.values.get("endTime")
        in_param = {"begin_time": begin_time,
                    "end_time": end_time
        }
        out_param = ps_list_cache_price.main(json.dumps(in_param))
        # return json.dumps(out_param)
        return render_template("list_cache_price.html", req=in_param, result=out_param)
    else:
        today = datetime.datetime.now()
        aweekago = today + datetime.timedelta(days=-7)
        in_param = {"begin_time": aweekago.strftime('%Y-%m-%d'),
                    "end_time": today.strftime('%Y-%m-%d')
                   }
        out_param = ps_list_cache_price.main(json.dumps(in_param))
        return render_template("list_cache_price.html", req=in_param, result=out_param)

@app.route('/detail_stat', methods=['GET', 'POST'])
def detail_stat():
    if request.method == "POST":
        begin_time = request.values.get("beginTime")
        end_time = request.values.get("endTime")
        show_type = request.values.get("showType")
        in_param = {"begin_time": begin_time,
                    "end_time": end_time,
                    "show_type": show_type
        }
        out_param = ps_detail_stat.main(json.dumps(in_param))
        # return json.dumps(out_param)
        return render_template("detail_stat.html", req=in_param, result=out_param)
    else:
        today = datetime.datetime.now()
        aweekago = today + datetime.timedelta(days=-7)
        in_param = {"begin_time": aweekago.strftime('%Y-%m-%d'),
                    "end_time": today.strftime('%Y-%m-%d'),
                    "show_type": '0'
                   }
        out_param = ps_detail_stat.main(json.dumps(in_param))
        return render_template("detail_stat.html", req=in_param, result=out_param)


@app.route('/price_change_stat', methods=['GET', 'POST'])
def price_change_stat():
    if request.method == "POST":
        begin_time = request.values.get("beginTime")
        end_time = request.values.get("endTime")
        show_type = request.values.get("showType")
        in_param = {"begin_time": begin_time,
                    "end_time": end_time,
                    "show_type": show_type
        }
        out_param = ps_price_change_stat.main(json.dumps(in_param))
        pic_data = {}
        if show_type == '0':
            day_data = []
            total_data = []
            spider_rate_data = []
            list_null_net_rate_data = []
            list_no_null_detail_null_net_rate_data = []
            pnc_ota_id_same_net_rate_data = []
            pnc_ota_id_differ_net_rate_data = []
            pc_ota_id_differ_list_no_detail_net_rate_data = []
            pc_ota_id_differ_detail_no_list_net_rate_data = []
            pc_ota_id_differ_list_detail_net_rate_data = []
            pc_ota_id_same_net_rate_data = []

            total = {}
            spider_rate = {}
            list_null_net_rate = {}
            list_no_null_detail_null_net_rate = {}
            pnc_ota_id_same_net_rate = {}
            pnc_ota_id_differ_net_rate = {}
            pc_ota_id_differ_list_no_detail_net_rate = {}
            pc_ota_id_differ_detail_no_list_net_rate = {}
            pc_ota_id_differ_list_detail_net_rate = {}
            pc_ota_id_same_net_rate = {}

            for r in out_param:
                day_data.append(str(r[0])[5:])  # 09-26
                total_data.append(int(r[1]))
                spider_rate_data.append(float(r[11]))
                list_null_net_rate_data.append(float(r[14]))
                list_no_null_detail_null_net_rate_data.append(float(r[16]))
                pnc_ota_id_same_net_rate_data.append(float(r[18]))
                pnc_ota_id_differ_net_rate_data.append(float(r[20]))
                pc_ota_id_differ_list_no_detail_net_rate_data.append(float(r[22]))
                pc_ota_id_differ_detail_no_list_net_rate_data.append(float(r[24]))
                pc_ota_id_differ_list_detail_net_rate_data.append(float(r[26]))
                pc_ota_id_same_net_rate_data.append(float(r[28]))

            # -- total
            total["color"] = 'purple'
            total["title_text"] = 'total'
            total["legend_data"] = 'legend_data'
            total["xAxis_data"] = day_data
            total["series_name"] = 'total'
            total["series_type"] = 'bar'
            total["series_data"] = total_data
            pic_data["total"] = total

            # -- spider_rate
            spider_rate["color"] = 'darkgreen'
            spider_rate["title_text"] = 'spider_rate'
            spider_rate["legend_data"] = 'legend_data'
            spider_rate["xAxis_data"] = day_data
            spider_rate["series_name"] = 'spider'
            spider_rate["series_type"] = 'bar'
            spider_rate["series_data"] = spider_rate_data
            pic_data["spider_rate"] = spider_rate

            # -- list_null_net_rate
            list_null_net_rate["color"] = 'blue'
            list_null_net_rate["title_text"] = 'list_null_net_rate'
            list_null_net_rate["legend_data"] = 'legend_data'
            list_null_net_rate["xAxis_data"] = day_data
            list_null_net_rate["series_name"] = 'list_null'
            list_null_net_rate["series_type"] = 'bar'
            list_null_net_rate["series_data"] = list_null_net_rate_data
            pic_data["list_null_net_rate"] = list_null_net_rate

            # -- list_no_null_detail_null_net_rate
            list_no_null_detail_null_net_rate["color"] = 'yellow'
            list_no_null_detail_null_net_rate["title_text"] = 'list_no_null_detail_null_net_rate'
            list_no_null_detail_null_net_rate["legend_data"] = 'legend_data'
            list_no_null_detail_null_net_rate["xAxis_data"] = day_data
            list_no_null_detail_null_net_rate["series_name"] = 'list_no_null_detail_null'
            list_no_null_detail_null_net_rate["series_type"] = 'bar'
            list_no_null_detail_null_net_rate["series_data"] = list_no_null_detail_null_net_rate_data
            pic_data["list_no_null_detail_null_net_rate"] = list_no_null_detail_null_net_rate

            # -- pnc_ota_id_same_net_rate
            pnc_ota_id_same_net_rate["color"] = 'red'
            pnc_ota_id_same_net_rate["title_text"] = 'pnc_ota_id_same_net_rate'
            pnc_ota_id_same_net_rate["legend_data"] = 'legend_data'
            pnc_ota_id_same_net_rate["xAxis_data"] = day_data
            pnc_ota_id_same_net_rate["series_name"] = 'pnc_ota_id_same'
            pnc_ota_id_same_net_rate["series_type"] = 'bar'
            pnc_ota_id_same_net_rate["series_data"] = pnc_ota_id_same_net_rate_data
            pic_data["pnc_ota_id_same_net_rate"] = pnc_ota_id_same_net_rate

            # -- pnc_ota_id_differ_net_rate
            pnc_ota_id_differ_net_rate["color"] = 'green'
            pnc_ota_id_differ_net_rate["title_text"] = 'pnc_ota_id_differ_net_rate'
            pnc_ota_id_differ_net_rate["legend_data"] = 'legend_data'
            pnc_ota_id_differ_net_rate["xAxis_data"] = day_data
            pnc_ota_id_differ_net_rate["series_name"] = 'pnc_ota_id_differ'
            pnc_ota_id_differ_net_rate["series_type"] = 'bar'
            pnc_ota_id_differ_net_rate["series_data"] = pnc_ota_id_differ_net_rate_data
            pic_data["pnc_ota_id_differ_net_rate"] = pnc_ota_id_differ_net_rate


            # -- pc_ota_id_differ_list_no_detail_net_rate
            pc_ota_id_differ_list_no_detail_net_rate["color"] = 'black'
            pc_ota_id_differ_list_no_detail_net_rate["title_text"] = 'pc_ota_id_differ_list_no_detail_net_rate'
            pc_ota_id_differ_list_no_detail_net_rate["legend_data"] = 'legend_data'
            pc_ota_id_differ_list_no_detail_net_rate["xAxis_data"] = day_data
            pc_ota_id_differ_list_no_detail_net_rate["series_name"] = 'pc_ota_id_differ_list_no_detail'
            pc_ota_id_differ_list_no_detail_net_rate["series_type"] = 'bar'
            pc_ota_id_differ_list_no_detail_net_rate["series_data"] = pc_ota_id_differ_list_no_detail_net_rate_data
            pic_data["pc_ota_id_differ_list_no_detail_net_rate"] = pc_ota_id_differ_list_no_detail_net_rate

            # -- pc_ota_id_differ_detail_no_list_net_rate
            pc_ota_id_differ_detail_no_list_net_rate["color"] = 'gray'
            pc_ota_id_differ_detail_no_list_net_rate["title_text"] = 'pc_ota_id_differ_detail_no_list_net_rate'
            pc_ota_id_differ_detail_no_list_net_rate["legend_data"] = 'legend_data'
            pc_ota_id_differ_detail_no_list_net_rate["xAxis_data"] = day_data
            pc_ota_id_differ_detail_no_list_net_rate["series_name"] = 'pc_ota_id_differ_detail_no_list'
            pc_ota_id_differ_detail_no_list_net_rate["series_type"] = 'bar'
            pc_ota_id_differ_detail_no_list_net_rate["series_data"] = pc_ota_id_differ_detail_no_list_net_rate_data
            pic_data["pc_ota_id_differ_detail_no_list_net_rate"] = pc_ota_id_differ_detail_no_list_net_rate


            # -- pc_ota_id_differ_list_detail_net_rate
            pc_ota_id_differ_list_detail_net_rate["color"] = 'brown'
            pc_ota_id_differ_list_detail_net_rate["title_text"] = 'pc_ota_id_differ_list_detail_net_rate'
            pc_ota_id_differ_list_detail_net_rate["legend_data"] = 'legend_data'
            pc_ota_id_differ_list_detail_net_rate["xAxis_data"] = day_data
            pc_ota_id_differ_list_detail_net_rate["series_name"] = 'pc_ota_id_differ_list_detail'
            pc_ota_id_differ_list_detail_net_rate["series_type"] = 'bar'
            pc_ota_id_differ_list_detail_net_rate["series_data"] = pc_ota_id_differ_list_detail_net_rate_data
            pic_data["pc_ota_id_differ_list_detail_net_rate"] = pc_ota_id_differ_list_detail_net_rate

            # -- pc_ota_id_same_net_rate
            pc_ota_id_same_net_rate["color"] = 'skyblue'
            pc_ota_id_same_net_rate["title_text"] = 'pc_ota_id_same_net_rate'
            pc_ota_id_same_net_rate["legend_data"] = 'legend_data'
            pc_ota_id_same_net_rate["xAxis_data"] = day_data
            pc_ota_id_same_net_rate["series_name"] = 'pc_ota_id_same'
            pc_ota_id_same_net_rate["series_type"] = 'bar'
            pc_ota_id_same_net_rate["series_data"] = pc_ota_id_same_net_rate_data
            pic_data["pc_ota_id_same_net_rate"] = pc_ota_id_same_net_rate
            dia_data = None
        else:
            dia_data = out_param
            pic_data = None
         
        # return json.dumps(pic_data)
        return render_template("price_change_stat.html", req=in_param, result = dia_data, picture = pic_data)
    else:
        in_param = {"begin_time": "2016-09-20",
                    "end_time": "2016-09-26",
                    "show_type": "0"
        }
        return render_template("price_change_stat.html", req=in_param, result=None)

@app.route('/sug', methods=['GET', 'POST'])
def sug():
    if request.method == "POST":
        input_str = request.values.get("input_str")
        in_param = {
            "input_str" : input_str
        }
        out_param = sug_test.main(json.dumps(in_param))
        # return json.dumps(out_param)
        return render_template("sug.html", req=in_param, result=out_param)
    else:
        in_param = {
            "input_str": "sug_test"
        }
        return render_template("sug.html", req=in_param, result=None)

@app.route('/sug1', methods=['GET', 'POST'])
def sug1():
    if request.method == "POST" or request.method == "GET":
        input_str = request.values.get("input_str")
        in_param = {
            "input_str" : input_str
        }
        out_param = sug_test.main(json.dumps(in_param))
        return render_template("sug1.html", req=in_param, result=out_param)


if __name__ == '__main__':
    app.run(host=server_ip, port=server_port, debug=True)
