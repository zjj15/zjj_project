from autost.api import *
DEV1="Gaea://127.0.0.1:5037/GFEDCBA0987654321"

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

# MMI OFF
sendCAN(BCM_A113.VehicleStates.phys, 0.0, interval=0.1, channel=CANBUS_CH2)
sendCAN(BCM_A112.ProbableCustomerFeedBackNeed.phys, 0.0, interval=0.1, channel=CANBUS_CH2)
#
sleep(20)
# MMI ON
sendCAN(BCM_A112.ProbableCustomerFeedBackNeed.phys, 1.0, interval=0.1, channel=CANBUS_CH2)
sendCAN(BCM_A113.VehicleStates.phys, 5.0, interval=0.1, channel=CANBUS_CH2)

#Check车机启动
assert_exists(Template('../../Design/Statusbar_Navi_0.png'), timeout=30)
sleep(20)
