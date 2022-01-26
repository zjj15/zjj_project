from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

try:
    assert_not_exists(Template('../../../Design/no_weather_info_icon.png'),device=DEV1,timeout=3)
except:
    error('check weather no info display !')