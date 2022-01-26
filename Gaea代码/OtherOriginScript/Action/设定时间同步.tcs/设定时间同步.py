from autost.api import *

import time

uri='Gaea://127.0.0.1:5037/GFEDCBA0987654321'

try:
    device(uri).adb.cmd("root")
    sleep(5)
    cur_time_fmtstr = time.strftime("%m%d%H%M%Y",time.localtime())
    print(cur_time_fmtstr)
    shell("date %s set"%cur_time_fmtstr)
except:
    print(__file__+' error')
