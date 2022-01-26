from autost.api import *

#冷启动
# off -> on
#sendCAN(BCM_A110.V_WakeUpSleepCommand.phys, 3.0, interval=0.1)
#sendCAN(BCM_A112.ProbableCustomerFeedBackNeed.phys, 1.0, interval=0.1)
##Max 4sec
#sleep(5)
#sendCAN(BCM_A113.VehicleStates.phys, 5.0, interval=0.1)
sendCAN(BCM_A110.V_WakeUpSleepCommand.phys, 3.0, interval=0.1)
sendCAN(BCM_A112.ProbableCustomerFeedBackNeed.phys, 1.0, interval=0.1)
sendCAN(BCM_A113.VehicleStates.phys, 5.0, interval=0.1)
sleep(30)
# 消息弹出："允许讯飞输入法访问您的通讯录吗"
for _ in range(4):
    if poco('允许', text='允许', timeout=1).exists():
        poco('允许', text='允许').click()
