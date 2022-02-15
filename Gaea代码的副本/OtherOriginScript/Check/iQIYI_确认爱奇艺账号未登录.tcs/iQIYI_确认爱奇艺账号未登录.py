from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print('__脚本名称: ' + __file__)

do_segment(Segment('../../Screen/进入iQIYI设置画面.tcs'))
poco('未登录', text='未登录').assert_exists()
poco('登录', text='登录').assert_exists()
