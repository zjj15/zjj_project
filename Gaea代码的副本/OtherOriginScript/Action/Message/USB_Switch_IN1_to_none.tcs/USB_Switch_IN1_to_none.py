from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print("__脚本名称: " + __file__)
# usb_switch(in, out)
# out=0, usb off状态
try:
    usb_switch(1, 0)
    sleep(1)
except:
    usb_off(1)
