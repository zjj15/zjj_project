from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
CANBUS_CH1 = 'CANBus2'
CANBUS_CH2 = 'MCAN'
print('__脚本名称: ' + __file__)
# Set ILL to 'Day'
sendCAN(METER_A104.DayNightForBacklights.phys, 0, interval=0.1, channel=CANBUS_CH1)
sleep(1)
