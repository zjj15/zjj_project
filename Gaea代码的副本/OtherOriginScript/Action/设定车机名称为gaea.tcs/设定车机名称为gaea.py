from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

flick([1000, 300], DIR_DOWN, step=3, speed=SPEED_NORMAL,device=DEV1)
flick([1000, 300], DIR_DOWN, step=3, speed=SPEED_NORMAL,device=DEV1)

touch(Template('../../Design/device_name_icon.png'),device=DEV1)
touch_if(Template('../../Design/input_Chinease_icon.png'), timeout=3,device=DEV1,threshold = 0.9)

# change device name to gaea
touch(Template('../../Design/input_English_g.png'),device=DEV1,threshold = 0.9)
touch(Template('../../Design/input_English_a.png'),device=DEV1,threshold = 0.9)
touch(Template('../../Design/input_English_e.png'),device=DEV1,threshold = 0.9)
touch(Template('../../Design/input_English_a.png'),device=DEV1,threshold = 0.9)
touch(Template('../../Design/input_complete_icon.png'),device=DEV1,threshold = 0.9)

# judge device name changed success
try:
    assert_exists(Template('../../Design/changed_device_name.png'),device=DEV1,threshold = 0.95)
except:
    error('change device name fail!') 
