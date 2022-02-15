from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'


try:
    assert_exists(Template("../../../Design/brightness_setting_min_icon.png"),device=DEV1)
except:
    error('check brightness min error!') 