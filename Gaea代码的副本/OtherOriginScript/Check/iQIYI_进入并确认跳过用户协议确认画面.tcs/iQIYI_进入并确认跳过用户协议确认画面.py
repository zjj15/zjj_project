from autost.api import *

do_segment(Segment('../../Common/BackHomeView.tcs'))

flick_to(Template('../../Design/Video_Picture_Card.png'), [970, 367], DIR_LEFT, step=1, speed=SPEED_NORMAL)
touch(Template('../../Design/Video_Picture_Card.png'), timeout=1)
touch_if(Template('../../Design/OnlineVideo_Login_cancel.png'), timeout=3)
if exists(Template('../../Design/OnlineVideo_Agreement_Confirm.png'), timeout=10):
    error("iQIYI_进入并确认跳过用户协议确认画面 error!!!")
