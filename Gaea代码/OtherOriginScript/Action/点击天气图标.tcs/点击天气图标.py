from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

touch([1026, 55],device=DEV1)

try:
    assert_not_exists(Template('../../Design/no_weather_info_icon.png'),device=DEV1,timeout=3)
except:
    error('网络差：weather no info display !')
