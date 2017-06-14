#!/usr/bin/env python
#-*- coding: utf-8 -*-

import random
import time
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Transaction(object):
    def __init__(self):
        pass

    def run(self):
        # cmd = "/home/work/itool/price/redis_test/redis/example/get"
        cmd = "/home/work/itool/price/redis_test/hiredis_vip/examples/mget1"
        # cmd = "/home/work/itool/price/redis_test/hiredis_master/examples/get"
        rs = os.popen(cmd).read()
        assert (rs is not None), 'WARNING: 结果为None'


if __name__ == '__main__':
    trans = Transaction()
    trans.run()
