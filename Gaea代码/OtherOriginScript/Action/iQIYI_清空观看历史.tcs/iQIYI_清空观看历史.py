from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'


if poco('是否清空全部观看历史？', text='是否清空全部观看历史？', timeout=1.5).exists():
    poco('是', text='是').click()
else:
    do_segment(Segment("../../Screen/进入iQIYI最近播放画面.tcs"))
    poco('观看历史', text='观看历史').click()
    if poco('清空', text='清空', timeout=1.5).exists():
        poco('清空', text='清空').click()
        poco('是', text='是').click()

touch_if(Template("../../Design/OnlineVideo_return_icon.png"), timeout=2, device=DEV1)
