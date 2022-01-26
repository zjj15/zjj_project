from autost.api import *
touch_if(Template('../../Design/OnlineVideo_Login_cancel.png'), timeout=1)
if exists(Template('../../Design/OnlineVideo_PlayScreen_Rate_1.png'), timeout=1):
    pass
else:
    do_segment(Segment('../../Screen/iQIYI_Rate设定画面.tcs'))
    if exists(Template('../../Design/OnlineVideo_RateScreen_1.png'), timeout=1):
        touch(Template('../../Design/OnlineVideo_RateScreen_1.png'), timeout=1)
    else:
        touch([683, 641])

try:
    assert_exists(Template('../../Design/OnlineVideo_PlayScreen_Rate_1.png'))
except:
    error('Setup OnlineVideo Rate 1 Error!')
