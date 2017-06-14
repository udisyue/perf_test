#!/usr/bin/env python
#-*- coding: utf-8 -*-

from google.protobuf import text_format
import sys
import struct
import socket
import random
import time
import datetime
import traceback
import logging

from gen import price_types_pb2
from gen import as_types_pb2
from gen import price_service_pb2 

#HOST = 'localhost'
HOST = '192.168.232.40'
PORT = 6300

logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%Y%m%d %H:%M:%S')

def build_message(nshead, in_param_dict):

    region_id = in_param_dict["region_id"]
    hotel_id_list = in_param_dict["hotel_id_list"]
    filter_ota = in_param_dict["filter_ota"]
    checkin = in_param_dict["checkin"]
    checkout = in_param_dict["checkout"]
    request_type = in_param_dict["request_type"]
    booking_channel = in_param_dict["booking_channel"]
    list_query_flag = in_param_dict["list_query_flag"]

    request = price_service_pb2.PsRequest()
    # search_id
    request.search_id = "12345678910"; 
    # version_id
    request.version_id = 1
    # user_info
    request.user_info.user_ip = "192.168.21.1"
    request.user_info.customer_level = 1
    request.user_info.order_from = 50
    request.user_info.booking_channel = booking_channel
    request.user_info.request_type = request_type
    # coupon info
    #request.user_info.activity_id_list.append(2015081441);
    #request.user_info.activity_id_list.append(2015081432);
    #request.user_info.activity_id_list.append(2015081457);
    #request.user_info.activity_id_list.append(2015081452);
    #request.user_info.activity_id_list.append(2015081460);
    #request.user_info.activity_id_list.append(2015081451);
    #request.user_info.activity_id_list.append(2015081513);
    # search_type
    request.service_type = 1
    # detail_req - query_info
    request.list_request.query_info.region_id = region_id
    for hid in hotel_id_list:
        request.list_request.query_info.hotel_id.append(hid)
    request.list_request.query_info.filter_ota = filter_ota
    request.list_request.query_info.cashpay_booking_channel_mask = 0
    room = request.list_request.query_info.room_person.add()
    room.adult_num  = 2
    # room.child_age_list.append(4)
    # room.child_age_list.append(2)
    # room.child_age_list.append(7)
    timeArray = time.strptime(checkin, "%Y-%m-%d")
    request.list_request.query_info.check_in_date = int(time.mktime(timeArray)) + 1000
    timeArray = time.strptime(checkout, "%Y-%m-%d")
    request.list_request.query_info.check_out_date = int(time.mktime(timeArray)) + 1000
    # request.list_request.query_info.check_in_date = 1477929600
    # request.list_request.query_info.check_out_date = 1478016000
    # list_query_flag
    # as请求ps可能的参数:
    # 3  0011 : ORIGIN_PRICE | ELONG_PRICE  - 列表页批量接口
    # 15 1111 : ORIGIN_PRICE | ELONG_PRICE | PROMOTION | DIGEST - 列表页批量接口
    # 1  0001 : ORIGIN_PRICE  - 列表页检索接口
    # 7  0111 : ORIGIN_PRICE | ELONG_PRICE | PROMOTION - 列表页检索接口
    request.list_request.query_info.list_query_flag = list_query_flag
    
    return request, request.SerializeToString(), request.ByteSize()

def handle_response(serialized_msg):
    # response = price_service_pb2.PsResponse()
    # response.ParseFromString(serialized_msg)
    # text_format.PrintMessage(response, sys.stdout)
    # return response
    return serialized_msg

def ps_list_query(in_param):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    nshead = struct.Struct("HHI16sIII");
    s.settimeout(20)
    response = None
        
    try:
        # connect
        s.connect((HOST, PORT))
        # send
        request, msg, length = build_message(nshead, in_param)
        head = nshead.pack(1, 1, 1, "elong", 1, 0, length)
        s.sendall(head)
        s.sendall(msg)
        # receive
        #time.sleep(1)
        data = s.recv(nshead.size)
        if len(data) == nshead.size:
            head_id, version, log_id, provider, magic, method_id, body_len = \
                nshead.unpack(data)
            
            if body_len != 0:
                serialized_msg = ""
                len_left = body_len
                while len_left > 0:
                    buf_size = len_left if len_left < 1024 else 1024
                    msg = s.recv(buf_size)
                    serialized_msg += msg
                    len_left -= len(msg);

                if body_len != len(serialized_msg) :
                    logging.warning("Received len(%d) != body_len(%d)", body_len,len(serialized_msg)) 
                else:
                    # logging.info("Received len: %d", len(serialized_msg))
                    response = handle_response(serialized_msg)
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
            in_param = {}
            in_param["region_id"] = 178236
            in_param["hotel_id_list"] = [288157,283641,284680,283698,283663,285419,283928,283624,287837,283646,283747,284654,283697,284661,283668]
            in_param["filter_ota"] = 33558912
            in_param["checkin"] = "2017-06-06"
            in_param["checkout"] = "2017-06-07"
            in_param["request_type"] = 1
            in_param["list_query_flag"] = 7
            in_param["booking_channel"] = 2
            time1 = time.time()
            rs = ps_list_query(in_param)
            assert (rs is not None), 'WARNING: 结果为None'
            time2 = time.time()
            logging.info("use time : %f", time2-time1)
        except KeyboardInterrupt:
            pass
        except Exception as e:
            logging.error(e)
            raise
