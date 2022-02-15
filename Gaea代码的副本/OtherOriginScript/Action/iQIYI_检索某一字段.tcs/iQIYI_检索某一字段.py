from autost.api import *

touch_if(Template('../../Design/OnlineVideo_PlayScreen_return.png'), timeout=1)

touch(Template('../../Design/OnlineVideo_Screen_Srch.png'))

touch(Template('../../Design/OnlineVideo_InputBox_Srch.png'))

touch(Template('../../Design/OnlineVideo_SrchKeyboard_y.png'),threshold = 0.8)
touch(Template('../../Design/OnlineVideo_SrchKeyboard_i.png'),threshold = 0.8)


for i in range(2):
    touch(Template('../../Design/OnlineVideo_SrchKeyboard_confirm.png'),threshold = 0.8)

for i in range(2):
    if not exists(Template('../../Design/OnlineVideo_Such_ywy.png'),threshold = 0.8):
        flick([957, 347], DIR_LEFT, step=1, speed=SPEED_NORMAL)

touch_if(Template('../../Design/OnlineVideo_Such_ywy.png'),threshold = 0.8, timeout=2)
'''
for i in range(3):
    touch(Template('../../Design/OnlineVideo_Such_ywy.png'),threshold = 0.8, timeout=2)
    if exists(Template('../../Design/OnlineVideo_走形规制_安全提示MSG.png'),threshold = 0.95, timeout = 2):
        do_segment(Segment('../DrivingRestrictOff.tcs'))

    if exists(Template('../../Design/OnlineVideo_Play_Bar.png'), timeout=30):
        break
    elif exists(Template('../../Design/OnlineVideo_暂停btn.png'), timeout=1):
        touch(Template('../../Design/OnlineVideo_暂停btn.png'), timeout=1)
        break
assert_exists(Template('../../Design/OnlineVideo_Play_ywy.png'),threshold = 0.95)
'''
