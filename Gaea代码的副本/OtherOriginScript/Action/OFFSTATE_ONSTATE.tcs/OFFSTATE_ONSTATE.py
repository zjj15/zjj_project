from autost.api import *

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
# OFF STATE
bup_off()
sleep(1)
bup_on()
sleep(3)
# C1A-HS ON
sendCAN(BCM_A110.V_WakeUpSleepCommand.phys, 3.0, interval=0.1, channel=CANBUS_CH2)
sendCAN(BCM_A112.ProbableCustomerFeedBackNeed.phys, 1.0, interval=0.1, channel=CANBUS_CH2)
sendCAN(BCM_A113.VehicleStates.phys, 5.0, interval=0.1, channel=CANBUS_CH2)

#2.Check车机启动
assert_exists(Template("../../Design/Statusbar_Navi_0.png"), timeout=30)
sleep(20)
