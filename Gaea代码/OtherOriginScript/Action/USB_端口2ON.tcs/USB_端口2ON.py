from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print("__脚本名称: " + __file__)

# usb端口1以外的端口，默认运行环境有黑盒子
# usb_switch(in, out)
usb_switch(1, 2)
