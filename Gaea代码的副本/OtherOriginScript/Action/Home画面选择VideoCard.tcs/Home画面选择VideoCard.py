from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print("__脚本名称: " + __file__)

do_segment(Segment("../../Common/BackHomeView.tcs"))

flick_to(Template("../../Design/Video_Picture_Card.png"), [970, 367], DIR_LEFT, step=1, speed=SPEED_NORMAL)
sleep(1)
for _ in range(3):
    touch_if(Template("../../Design/Video_Picture_Card.png"), timeout=1)
