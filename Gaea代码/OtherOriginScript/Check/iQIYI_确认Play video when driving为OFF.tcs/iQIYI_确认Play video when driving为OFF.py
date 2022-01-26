from autost.api import *

touch_if(Template("../../Design/OnlineVideo_Login_cancel.png"), timeout=1)

flick_to(Template('../../Design/Setting_PlayVideo_Driving.png'), [988, 460], DIR_UP, step=1, speed=SPEED_NORMAL)

try:
    assert_exists(Template('../../Design/Setting_PlayVideo_Driving_OFF.png'))
except:
    error('PlayVideo When Driving Switch OFF Check Error!')

