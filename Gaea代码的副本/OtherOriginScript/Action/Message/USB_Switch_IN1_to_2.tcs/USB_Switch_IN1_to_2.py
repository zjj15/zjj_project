from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print("__脚本名称: " + __file__)

# usb_switch(in, out)
# out=1, 插入U盘（无可播放文件）
usb_switch(1, 2)
