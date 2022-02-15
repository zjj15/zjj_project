from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print("__脚本名称: " + __file__)

assert_exists(Template('../../Design/StatusBar_KTV.png'), device=DEV1)
