from autost.api import *
do_segment(Segment('../../Common/BackHomeView.tcs'))

flick_to(Template('../../Design/Video_Picture_Card.png'), [970, 367], DIR_LEFT, step=1, speed=SPEED_NORMAL)
sleep(1)
touch(Template('../../Design/Video_Picture_Card.png'), timeout=5)
touch_if(Template('../../Design/OnlineVideo_Login_cancel.png'), timeout=1)