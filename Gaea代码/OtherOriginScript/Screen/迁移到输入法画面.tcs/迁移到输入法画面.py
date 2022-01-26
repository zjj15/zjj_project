from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

#进入其他Source
do_segment(Segment('../迁移到中控设定画面.tcs'))
for i in range(3):
    flick([238, 667], DIR_UP, step=1, speed=SPEED_NORMAL,device=DEV1)
    if exists(Template('../../Design/otherSetting_selected_icon.png'),device=DEV1, timeout=2) or exists(Template('../../Design/otherSetting_icon.png'),device=DEV1, timeout=2):
        break

touch_if(Template('../../Design/otherSetting_icon.png'), timeout=3,device=DEV1)
touch_if(Template('../../Design/otherSetting_devicename.png'), timeout=3,device=DEV1)
try:
    assert_exists(Template('../../Design/Input_del_ok.png'),device=DEV1)
except:
    error('IntoOtherSetting error!')
