from autost.api import *

#前置条件
##打开USB端口
do_segment(Segment('../USB_端口1ON.tcs'))

touch(Template('../../Design/FaultDiag_Comfirm_Adjust.png'))

flick_to(Template('../../Design/FaultDiag_ScreenShot_USB.png'), [1185, 365], DIR_UP, step=1, speed=SPEED_NORMAL, timeout=30)

sleep(1)
touch(Template('../../Design/FaultDiag_ScreenShot_USB.png'))

touch_if(Template('../../Design/ScreenShot_USB_ON_nofocus.png'), timeout=2)
if exists(Template('../../Design/ScreenShot_USB_noUSBDevice.png'), timeout=3):
    touch(Template('../../Design/ScreenShot_USB_confirm.png'))

try:
    assert_exists(Template('../../Design/ScreenShot_USB_ON_res.png'))
except:
    error('ScreenShot USB ON Error!')
