from autost.api import *

DEV1="Gaea://127.0.0.1:5037/GFEDCBA0987654321"

def enter_screen():
    do_segment(Segment('../../Common/BackHomeView.tcs'))
    ## for the case：车机重启,延长timeout
    flick_to(Template('../../Design/More_Card.png'), [957, 347], DIR_LEFT, step=1, speed=SPEED_NORMAL, timeout=50)
    touch_if(Template('../../Design/More_Card.png'), timeout=2)
    touch_if(Template('../../Design/Setting_Card.png'), timeout=2)

if exists(Template('../../Design/ShortBar_Setting_focus_old_noword.png'), timeout=3):
    pass
else:
    ## for the case：车机重启，bt重连ons弹出，进入失败
    for _ in range(5):
        enter_screen()
        touch_if(Template('../../Design/ShortBar_Setting_nofocus_noword.png'), timeout=1)
        touch_if(Template('../../Design/ShortBar_Setting_nofocus_noword.png'), timeout=1)
        if exists(Template('../../Design/ShortBar_Setting_focus_old_noword.png'), timeout=2):
            break
assert_exists(Template('../../Design/ShortBar_Setting_focus_old_noword.png'), timeout=5)
#if poco('确定', text='确定', timeout=1).exists():
#    poco('确定', text='确定', timeout=1).click()

