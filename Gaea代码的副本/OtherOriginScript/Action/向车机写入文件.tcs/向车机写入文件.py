from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
print("__脚本名称: " + __file__)


try:
    shell('dd if=/dev/zero of=/sdcard/zero bs=1024 count=6500000')
except:
    print('写入文件 exception')
