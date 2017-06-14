#!/usr/bin/env python
#-*- coding: utf-8 -*-

import random
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("./ps_stress_test/test_scripts/unitTest")

from ps_detail import ps_detail_query

class Transaction(object):
    def __init__(self):
        pass

    def run(self):
        in_param = {
            "server_ip": "10.39.136.17",
            "port":6300,
            "hotel_id": 324864,
            "filter_ota": 857668526, 
            "checkin": "2017-06-06",
            "checkout": "2017-06-07",
            "booking_channel": 4,
            "request_type": 3
        }
        rs = ps_detail_query(in_param)
        assert (rs is not None), 'WARNING: 结果为None'


if __name__ == '__main__':
    trans = Transaction()
    trans.run()
