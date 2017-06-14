#!/usr/bin/env python
#-*- coding: utf-8 -*-

import random
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("./ps_stress_test/test_scripts/unitTest")

from ps_booking import ps_booking_query

class Transaction(object):
    def __init__(self):
        pass

    def run(self):
        in_param = {
            "booking_channel" : 4,
            "hotel_id" : 326482,
            "filter_ota" : 33558912,
            "checkin" : "2017-06-06",
            "checkout" : "2017-06-07",
            "request_type" : 1,
            "ota_id" : 7,
            "source_ota_id" : -1,
            "elong_pname" : "0",
            "elong_pid" : 5793500019080690985,
            "ota_sign" : 1862440793830612744
        }
        rs = ps_booking_query(in_param)
        print len(rs)
        assert (rs is not None), 'WARNING: 结果为None'


if __name__ == '__main__':
    trans = Transaction()
    trans.run()
