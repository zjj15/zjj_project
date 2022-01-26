from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

if poco('是否清空全部收藏内容？', text='是否清空全部收藏内容？', timeout=1.5).exists():
    poco('是', text='是').click()
else:
    do_segment(Segment("../../Screen/进入iQIYI我的收藏画面.tcs"))
    poco('我的收藏', text='我的收藏').click()
    if poco('清空', text='清空', timeout=1.5).exists():
        poco('清空', text='清空').click()
        poco('是', text='是').click()

touch_if(Template('../../Design/OnlineVideo_return_icon.png'), timeout=3,device=DEV1)
