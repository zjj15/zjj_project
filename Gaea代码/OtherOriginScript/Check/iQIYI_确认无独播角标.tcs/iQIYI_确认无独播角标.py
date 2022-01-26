from autost.api import *

def check():
    if exists(Template('../../Design/OnlineVideo_独播_icon.png'), timeout=1,threshold = 0.88) or exists(Template('../../Design/OnlineVideo_独播_大icon.png'), timeout=1,threshold = 0.88):
        error('iQIYI_确认无独播角标表示 error')

touch_if(Template('../../Design/OnlineVideo_Login_cancel.png'), timeout=1)
check()
if exists(Template('../../Design/OnlineVideo_画面位置_进度靠左.png'), timeout=2) or exists(Template('../../Design/OnlineVideo_画面位置_靠左.png'), timeout=2,threshold = 0.96):
    for i in range(9):
        flick([1430, 454], DIR_LEFT, step=2, speed=SPEED_FAST)
        check()
else:
    for i in range(9):
        flick([600, 454], DIR_RIGHT, step=2, speed=SPEED_FAST)
        check()