from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print('__脚本名称: ' + __file__)

try:
    assert_exists(Template('../../Design/weather_city_name.png'), threshold=0.90, device=DEV1)
except:
    error('__脚本名称: ' + __file__+ 'Check error')
