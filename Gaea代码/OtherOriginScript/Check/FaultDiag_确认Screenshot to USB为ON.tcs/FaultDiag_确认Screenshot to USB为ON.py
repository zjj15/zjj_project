from autost.api import *

touch(Template('../../Design/FaultDiag_Comfirm_Adjust.png'))

flick_to(Template('../../Design/FaultDiag_ScreenShot_USB.png'), [1185, 365], DIR_UP, step=1, speed=SPEED_NORMAL, timeout=30)
sleep(1)
touch(Template('../../Design/FaultDiag_ScreenShot_USB.png'))

try:
    assert_exists(Template('../../Design/ScreenShot_USB_ON_res.png'))

except:
    error('FaultDiag ScreenShot to USB Swtich ON Error!')
