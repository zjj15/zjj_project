from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

print('__脚本名称: ' + __file__)

try:
    assert_not_exists(Template('../../Design/IME_BTPhone_keyboard_icon.png'), threshold=0.90, device=DEV1,timeout=5)
except:
    error('__脚本名称: ' + __file__+ 'Check error')
