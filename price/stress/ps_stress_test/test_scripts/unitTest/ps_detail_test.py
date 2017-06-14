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

HOST = 'localhost'
# HOST = '10.39.135.17'
PORT = 6300

def build_message(nshead, in_param_dict):
    # get param
    booking_channel = in_param_dict["booking_channel"]
    hotel_id = in_param_dict["hotel_id"]
    filter_ota = in_param_dict["filter_ota"]
    checkin = in_param_dict["checkin"]
    checkout = in_param_dict["checkout"]
    request_type = in_param_dict["request_type"]

    request = price_service_pb2.PsRequest()
    request.search_id = "12345678910"; 
    request.version_id = 2
    request.service_type = 2

    # user_info
    request.user_info.user_ip = "127.0.0.1"
    request.user_info.customer_level = 0
    request.user_info.order_from = 0
    request.user_info.booking_channel = booking_channel
    request.user_info.request_type = request_type

    # query_info
    request.detail_request.query_info.hotel_id.append(hotel_id)
    request.detail_request.query_info.filter_ota = filter_ota
    room = request.detail_request.query_info.room_person.add()
    room.adult_num  = 2
    timeArray = time.strptime(checkin, "%Y-%m-%d")
    request.detail_request.query_info.check_in_date = int(time.mktime(timeArray)) + 1000
    timeArray = time.strptime(checkout, "%Y-%m-%d")
    request.detail_request.query_info.check_out_date = int(time.mktime(timeArray)) + 1000
    # request.detail_request.query_info.cache_time = 1000
    # request.detail_request.query_info.timeout = 3000

    # 不参与优选
    request.detail_request.query_info.preferred_product = False
    
    return request.SerializeToString(), request.ByteSize()

def handle_response(serialized_msg):
    return serialized_msg
    # response = price_service_pb2.PsResponse()
    # response.ParseFromString(serialized_msg)
    # text_format.PrintMessage(response, sys.stdout)
    # return response

# in_param must be dict!
def ps_detail_query(in_param):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(20)
    nshead = struct.Struct("HHI16sIII");
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
        # print "len ============", len(data)
        if len(data) == nshead.size:
            head_id, version, log_id, provider, magic, method_id, body_len = \
                nshead.unpack(data)
            # print "body len ============", body_len
            total = 0
            if body_len != 0:
                serialized_msg = ""
                len_left = body_len
                while len_left > 0:
                    buf_size = len_left if len_left < 1024 else 1024
                    serialized_msg += s.recv(buf_size)
                    len_left -= buf_size;
                    total += buf_size
                  
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
            in_param["filter_ota"] = 174
            # in_param["filter_ota"] = 857669550
            in_param["checkin"] = "2017-06-06"
            in_param["checkout"] = "2017-06-07"
            in_param["request_type"] = 3
            time1 = time.time()
            rs = ps_detail_query(in_param)
            assert (rs is not None), 'WARNING: 结果为None' 
            time2 = time.time()
            print "use time : ", time2-time1
        except KeyboardInterrupt:
            pass
        except Exception as e:
            logging.error(e)
            raise
