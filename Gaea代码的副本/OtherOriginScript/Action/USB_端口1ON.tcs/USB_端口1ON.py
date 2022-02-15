from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print("__脚本名称: " + __file__)

try:
    # usb_switch(in, out)
    usb_switch(1, 1)
except:
    # 外设缺少：黑盒子，使用usb_on接口
    usb_on(1)

