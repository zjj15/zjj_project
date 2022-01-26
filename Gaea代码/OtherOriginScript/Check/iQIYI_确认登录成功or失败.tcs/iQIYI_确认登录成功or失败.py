from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print('__脚本名称: ' + __file__)

do_segment(Segment("../../Screen/进入iQIYI设置画面.tcs"))
if poco('未登录', text='未登录').exists():
    pass
else:
    pass