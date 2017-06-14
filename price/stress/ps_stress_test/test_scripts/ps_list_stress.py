#!/usr/bin/env python
#-*- coding: utf-8 -*-

import random
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("./ps_stress_test/test_scripts/unitTest")

from ps_list import ps_list_query

class Transaction(object):
    def __init__(self):
        pass

    def run(self):
        in_param = {
            "region_id" : 178236,
            "hotel_id_list" : [288157,283641,284680,283698,283663,285419,283928,283624,287837,283646,283747,284654,283697,284661,283668],
            "filter_ota" : 33558912,
            "checkin" : "2017-06-06",
            "checkout" : "2017-06-07",
            "request_type" : 1,
            "list_query_flag" : 7,
            "booking_channel" : 4
        }
        rs = ps_list_query(in_param)
        assert (rs is not None), 'WARNING: 结果为None'


if __name__ == '__main__':
    trans = Transaction()
    trans.run()
