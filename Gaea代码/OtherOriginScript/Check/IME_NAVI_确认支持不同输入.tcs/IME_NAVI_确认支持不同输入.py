from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

try:
    assert_exists(Template('../../Design/IME_Navi_input.png'), threshold=0.90)
except:
    error('__脚本名称: ' + __file__+ 'Check error')
