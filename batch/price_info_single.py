#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
from google.protobuf import text_format
import logging
import struct
import socket
import random
import time
import datetime
import traceback
import json

from gen import price_types_pb2
from gen import as_types_pb2
from gen import price_service_pb2 

HOST = "192.168.94.60"
PORT = 6300
# MONTH_LIST = ["2016-12", "2017-01", "2017-02", "2017-03", "2017-04", "2017-05", "2017-06", "2017-07", "2017-08", "2017-09", "2017-10", "2017-11"]
MONTH_LIST = ["2016-12"] 

def build_message(nshead, in_param_dict):
    request = price_service_pb2.PsRequest()
    # search_type
    request.service_type = 1
    # search_id
    request.search_id = "987654321static"; 
    # version_id
    request.version_id = 2
    # user_info
    request.user_info.user_ip = "127.0.0.1"
    request.user_info.customer_level = 0
    request.user_info.order_from = 0
    request.user_info.booking_channel = 2
    # list_req - query_info
    for hid in in_param_dict["hotel_id"].split(','):
        if hid != '':
            request.list_request.query_info.hotel_id.append(int(hid))
    request.list_request.query_info.filter_ota = 982958
    request.list_request.query_info.cashpay_booking_channel_mask = 0
    room = request.list_request.query_info.room_person.add()
    room.adult_num  = 2
    timeArray = time.strptime(in_param_dict["checkin"], "%Y-%m-%d")
    request.list_request.query_info.check_in_date = int(time.mktime(timeArray)) + 1000
    timeArray = time.strptime(in_param_dict["checkout"], "%Y-%m-%d")
    request.list_request.query_info.check_out_date = int(time.mktime(timeArray)) + 1000
    # list_query_flag
    # 1  0001 : ORIGIN_PRICE  - 列表页检索接口
    # 3  0011 : ORIGIN_PRICE | ELONG_PRICE  - 列表页批量接口
    # 15 1111 : ORIGIN_PRICE | ELONG_PRICE | PROMOTION | DIGEST - 列表页批量接口
    # 7  0111 : ORIGIN_PRICE | ELONG_PRICE | PROMOTION - 列表页检索接口
    request.list_request.query_info.list_query_flag = 1
    
    return request.SerializeToString(), request.ByteSize()

def handle_response(serialized_msg, in_param_dict):
    try:
        response = price_service_pb2.PsResponse()
        response.ParseFromString(serialized_msg)
    except Exception as e:
        print "fail", len(serialized_msg)

    if response.list_response and response.list_response.list_hotel:
       # for lh in response.list_response.list_hotel:
       #     # 1. sold out
       #     if lh.booking_status == 1:
       #         print "%d_%s_%d" % (lh.base_hotel_id, in_param_dict["month"], 1)
       #     else:
       #         print "%d_%s_%d" % (lh.base_hotel_id, in_param_dict["month"], 0)
       print "success", len(serialized_msg)

def main(in_param):
    nshead = struct.Struct("HHI16sIII");
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    response = None
        
    try:
        # connect
        s.connect((HOST, PORT))
        # send
        msg, length = build_message(nshead, in_param)
        head = nshead.pack(1, 1, 1, "elong", 1, 0, length)
        s.sendall(head)
        s.sendall(msg)
        # receive
        data = s.recv(nshead.size)
        # print len(data)
        if len(data) == nshead.size:
            head_id, version, log_id, provider, magic, method_id, body_len = \
                nshead.unpack(data)
            
            if body_len != 0:
                serialized_msg = ""
                len_left = body_len
                while len_left > 0:
                    buf_size = len_left if len_left < 1024 else 1024
                    serialized_msg += s.recv(buf_size)
                    len_left -= buf_size;
                  
                response = handle_response(serialized_msg, in_param)
            else:
                logging.warning("Received an empty message")
        else:
            logging.warning("Receive bad nshead header, length=%d", len(data))

        s.close()
    except socket.error, e:
        logging.warning(e)
        traceback.print_exc()
    finally:
        s.close()
    return response
    

if __name__ == '__main__':
        try:
            index = 0
            hids = ""
            in_param = {}
            time1 = time.time()
            with open("data/hotel_id_list") as rf:
                for line in rf.readlines():
                    hids = hids + line.strip() + ","
                    index = index + 1
                    if 150 == index:
                        for m in MONTH_LIST:
                            in_param["checkin"] = "%s-15" % m
                            in_param["checkout"] = "%s-16" % m
                            in_param["hotel_id"] = hids
                            in_param["month"] = m.split('-')[1]
                            main(in_param)
                        break
                        index = 0
                        hids = ""
            time2 = time.time()
            print "use time : ", time2-time1
        except KeyboardInterrupt:
            pass
        except Exception as e:
            logging.error(e)
            raise
