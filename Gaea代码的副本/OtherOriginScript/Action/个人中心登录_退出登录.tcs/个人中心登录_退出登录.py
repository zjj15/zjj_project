from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
# 迁移到个人中心画面
do_segment(Segment("../../Screen/迁移到个人中心画面.tcs"))

if poco('账号', text='账号').exists():
    poco('账号', text='账号').click()
    poco('退出', text='退出').click()
    poco('坚持退出', text='坚持退出').click()
