from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
print("__脚本名称: " + __file__)

#将设备空间塞满
try:
    shell('dd if=/dev/zero of=/sdcard/zero bs=1024 count=7892000')
except:
    print('割入_MSG_设备空间满 exception')
