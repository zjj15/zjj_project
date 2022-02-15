from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

try:
    assert_exists(Template('../../Design/24hour_setting_off_icon.png'),device=DEV1)
except:
    error('check 24hour setting off fail!') 