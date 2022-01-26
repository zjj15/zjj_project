from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print("__脚本名称: " + __file__)

# usb_switch(in, out)
# out=1, 插入U盘（版本信息文件错误）
try:
    usb_switch(1, 1)
    sleep(1)
except:
    usb_on(1)
    sleep(1)
