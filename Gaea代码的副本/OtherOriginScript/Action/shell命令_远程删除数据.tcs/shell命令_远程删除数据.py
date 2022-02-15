from autost.api import *

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

shell('am broadcast -a iauto.system.csagent.beginwipe')
sleep(1)