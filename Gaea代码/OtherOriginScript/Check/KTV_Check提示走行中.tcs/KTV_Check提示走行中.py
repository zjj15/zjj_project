from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print("__脚本名称: " + __file__)

assert_exists(Template('../../Design/KTV_safety_tip.png'), device=DEV1,threshold = 0.8)