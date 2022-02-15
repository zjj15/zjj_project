from autost.api import *

#前置条件
##打开USB端口
do_segment(Segment("../../Action/USB_端口1ON.tcs"))

do_segment(Segment("../../Common/BackHomeView.tcs"))

flick_to(Template("../../Design/Music_Card.png"), [971, 353], DIR_LEFT, step=1, speed=SPEED_NORMAL)

touch(Template("../../Design/Music_Card.png"))

touch_if(Template("../../Design/Music_USBAudio_btn_nofocus.png"), timeout=2)

touch_if(Template("../../Design/ShortBar_iPod_nofocus.png"), timeout=3)
