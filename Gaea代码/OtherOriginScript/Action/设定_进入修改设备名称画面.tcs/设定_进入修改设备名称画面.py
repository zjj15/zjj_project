from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

flick([1000, 300], DIR_DOWN, step=3, speed=SPEED_NORMAL,device=DEV1)
flick([1000, 300], DIR_DOWN, step=3, speed=SPEED_NORMAL,device=DEV1)

touch(Template('../../Design/device_name_icon.png'),device=DEV1)


# judge device name changed success
try:
    assert_exists(Template('../../Design/IME_BTPhone_keyboard_icon.png'),device=DEV1,threshold = 0.95)
except:
    error('enter change device name screen fail!') 
