from autost.api import *

DEV1 = 'iAndroid://127.0.0.1:5037/GFEDCBA0987654321'
DEV3 = 'AndroidMB0087://127.0.0.1:5037/RKKDU18410004307'

#setting phone BT on
do_segment(Segment('../MB0087_BT_On.tcs'))

#setting vehicle BT on
do_segment(Segment('../VehicleBTOn.tcs'))

#action:connect MiA1
touch_if(Template('pic/capture_20210312194609450120.png'), threshold=0.90, device=DEV1,timeout=4)

sleep(2)
if exists(Template('pic/capture_20210312194453006229.png'), device=DEV3):
    touch_if(Template('pic/capture_20210312185606921952.png'), device=DEV3,timeout=2)
    touch(Template('pic/capture_20210312194505066200.png'), device=DEV3)
    sleep(2)
    touch_if(Template('pic/capture_20210312194524849535.png'), device=DEV3,timeout=3)

#Check:conncect success
try:
    assert_exists(Template('pic/capture_20210312194834786281.png'), threshold=0.90, device=DEV1,timeout=10)
except:
    error('conncect AndroidMB0087 device failed!!!')
 


