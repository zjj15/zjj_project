from autost.api import *

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
# REV OFF
sendCAN(USM_A101.RearGearEngaged.phys, 0.0, interval=0.1, channel=CANBUS_CH2)
sleep(2)
