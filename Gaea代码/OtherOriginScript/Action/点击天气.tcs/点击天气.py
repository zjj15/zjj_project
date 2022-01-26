from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

touch([1026, 55],device=DEV1)
if exists(Template('../../Design/no_weather_info_icon.png'),device=DEV1,timeout=2):
    do_segment(Segment('../设定时间同步.tcs'))
    sleep(2)
    touch([1026, 55],device=DEV1)

try:
    assert_not_exists(Template('../../Design/no_weather_info_icon.png'),device=DEV1,timeout=1)
except:
    error('weather no info display !')
