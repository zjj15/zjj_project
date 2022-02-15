from autost.api import *

do_segment(Segment('../../Common/BackHomeView.tcs'))

flick_to(Template('../../Design/Video_Picture_Card.png'), [970, 367], DIR_LEFT, step=1, speed=SPEED_NORMAL)
touch(Template('../../Design/Video_Picture_Card.png'), timeout=5)
for i in range(3):
    touch_if(Template('../../Design/OnlineVideo_Login_cancel.png'), timeout=1)
    if poco('在线视频', text='在线视频', timeout=2).exists():
        poco('在线视频', text='在线视频', timeout=4).click()
if poco('允许', text='允许', timeout=1).exists():
    for _ in range(3):
        if poco('允许', text='允许', timeout=1).exists():
            poco('允许', text='允许').click()
            sleep(0.5)