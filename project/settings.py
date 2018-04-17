# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 下午10:38
# @Author  : xiaoqingtang
# @Site    : 
# @File    : settings.py.py

import os
basedir = os.path.abspath(os.path.dirname(__file__))

# initialize configuration based on environment
profile = os.getenv('PROFILE', 'local')

print "environment {} configuration loaded".format(profile)
if profile == 'product':
    from conf.config_prod import *
elif profile == 'test':
    from conf.config_test import *
else:
    from conf.config_local import *