from autost.api import *

acc_off()
sleep(ST.acc_off_sleep_time)
acc_on(uri=ST.DEV1)
'''
if exists(Template('pic/StartUp.png'), timeout = ST.system_startUp_Time, device=ST.DEV1):
    pass
else:
    error('start failed or time out')
'''