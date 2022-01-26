from autost.api import *

# 1,等待adb device与ide连接
print("wait for device start")
uri='Gaea://127.0.0.1:5037/GFEDCBA0987654321'
device(uri).adb.wait_for_device(timeout=60)
print("wait for device end")

say(Audio('audio/Music.wav'))

sleep(5)



