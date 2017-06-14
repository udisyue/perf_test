#!/usr/bin/env python
#-*- coding: utf-8 -*-

from google.protobuf import text_format
import sys
import logging
import struct
import socket
import random
import time
import datetime
import traceback

from gen import price_types_pb2
from gen import as_types_pb2
from gen import price_service_pb2 

HOST = 'localhost'
# HOST = '192.168.232.40'
PORT = 6300

logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%Y%m%d %H:%M:%S')

def build_message(nshead, in_param_dict):

    # get param
    booking_channel = in_param_dict["booking_channel"]
    hotel_id = in_param_dict["hotel_id"]
    filter_ota = in_param_dict["filter_ota"]
    checkin = in_param_dict["checkin"]
    checkout = in_param_dict["checkout"]
    request_type = in_param_dict["request_type"]
    ota_id = in_param_dict["ota_id"]
    source_ota_id = in_param_dict["source_ota_id"]
    elong_pname = in_param_dict["elong_pname"]
    elong_pid = in_param_dict["elong_pid"]
    ota_sign = in_param_dict["ota_sign"]

    request = price_service_pb2.PsRequest()
    # search_id
    request.search_id = "12345678910" 
    # version_id
    request.version_id = 2
    # user_info
    request.user_info.user_ip = "192.168.21.1"
    request.user_info.customer_level = 2
    request.user_info.order_from = 2
    request.user_info.booking_channel = booking_channel
    request.user_info.request_type = request_type
    # search_type
    request.service_type = 3
    #booking_req - query_info
    request.booking_request.query_info.hotel_id.append(hotel_id)
    request.booking_request.query_info.filter_ota = filter_ota
    room = request.booking_request.query_info.room_person.add()
    room.adult_num  = 2
    # room.child_age_list.append(4)
    # room.child_age_list.append(2)
    # room.child_age_list.append(7)
    timeArray = time.strptime(checkin, "%Y-%m-%d")
    request.booking_request.query_info.check_in_date = int(time.mktime(timeArray)) + 1000
    timeArray = time.strptime(checkout, "%Y-%m-%d")
    request.booking_request.query_info.check_out_date = int(time.mktime(timeArray)) + 1000

    # detail_ota --- ota
    request.booking_request.detail_ota.base_hotel_id = hotel_id
    request.booking_request.detail_ota.ota_id = ota_id;
    request.booking_request.detail_ota.hotel_status = 1
    # detail_ota --- room
    room = request.booking_request.detail_ota.room_list.add()
    room.room_id = 40239018
    room.room_name_cn = "标准双人房"
    room.room_status = 1
    # detail_ota --- product
    product = room.product_list.add()
    product.room_num = 1
    product.elong_pid = elong_pid
    product.ota_sign = ota_sign
    product.source_ota_id = source_ota_id
    product.elong_pname = elong_pname

    return request, request.SerializeToString(), request.ByteSize()

def handle_response(serialized_msg):
    # response = price_service_pb2.PsResponse()
    # response.ParseFromString(serialized_msg)
    # text_format.PrintMessage(response, sys.stdout)
    # return response
    return serialized_msg

def ps_booking_query(in_param):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(20)
    nshead = struct.Struct("HHI16sIII");
    response =  None
        
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
            in_param["booking_channel"] = 2
            in_param["hotel_id"] = 326482
            in_param["filter_ota"] = 33558912
            in_param["checkin"] = "2017-06-06"
            in_param["checkout"] = "2017-06-07"
            in_param["request_type"] = 1
            in_param["ota_id"] = 7
            in_param["source_ota_id"] = -1 
            in_param["elong_pname"] = "0" 
            in_param["elong_pid"] = 5793500019080690985
            in_param["ota_sign"] = 1862440793830612744
            time1 = time.time()
            rs = ps_booking_query(in_param)
            time2 = time.time()
            assert (rs is not None), 'WARNING: 结果为None'
            logging.info("use time : %f", time2-time1)
        except KeyboardInterrupt:
            pass
        except Exception as e:
            logging.error(e)
            raise
