from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

touch([1709, 184],device=DEV1)

try:
    assert_exists(Template('../../Design/brightness_setting_max_icon.png'),device=DEV1)
except:
    error('set brightness max error!') 

