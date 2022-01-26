from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print("__脚本名称: " + __file__)

# 1,等待adb device与ide连接
print("wait for device start")
uri='Gaea://127.0.0.1:5037/GFEDCBA0987654321'
device(uri).adb.wait_for_device(timeout=60)
print("wait for device end")

try:
    # usb_switch(in, out)
    for _ in range(4):
        usb_switch(1, 0)
        usb_switch(1, 1)
    sleep(5)
except:
    # 外设缺少：黑盒子，使用usb_on接口
    for _ in range(4):
        usb_off(1)
        usb_on(1)
    sleep(5)
