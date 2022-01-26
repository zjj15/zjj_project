from autost.api import *

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
DEV1 = ST.DEV1
#B+ OFF
##ON STATE ->  MMI OFF STATE
###VehicleStates = OFF && ProbableCustomerFeedBackNeed = Customer feedback probably not needed except E-CALL(Manual or ACN) mode
stopCAN(BCM_A113.VehicleStates.phys, 0.0, interval=0.1, device=DEV1)
stopCAN(BCM_A112.ProbableCustomerFeedBackNeed.phys, 0.0, interval=0.1, device=DEV1)

###Max100ms
sleep(1)

##MMI OFF STATE -> OFF STATE
###V_WakeUpSleepCommand = Go to Sleep
stopCAN(BCM_A110.V_WakeUpSleepCommand.phys, 0.0, interval=0.1, device=DEV1)

###Max 4sec
sleep(5)

#B+off -> on
bup_off()
sleep(4)
bup_on()
sleep(2)

#冷启动
##OFF STATE ->  MMI OFF STATE
sendCAN(BCM_A110.V_WakeUpSleepCommand.phys, 3, BCM_A110.V_WakeUpType.phys, 0, interval=0.1, device=DEV1)
#sendCAN(BCM_A113.DeliveryModeInformation_v2.phys, 0, interval=0.1, device=DEV1)

##Max 4sec
sleep(5)

##MMI OFF STATE ->  ON STATE
sendCAN(BCM_A112.ProbableCustomerFeedBackNeed.phys, 1.0, interval=0.1, device=DEV1)
sendCAN(BCM_A113.VehicleStates.phys, 5, interval=0.1, device=DEV1)
#游客登录
sleep(8)
