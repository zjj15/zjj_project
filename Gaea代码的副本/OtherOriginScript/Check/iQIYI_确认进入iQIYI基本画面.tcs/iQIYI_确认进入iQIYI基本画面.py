from autost.api import *
touch_if(Template("../../Design/OnlineVideo_Login_cancel.png"), timeout=1)
try:
    assert_exists(Template('../../Design/ShortBar_OnlineVideo_focus.png'))
    assert_exists(Template('../../Design/OnlineVideo_Center.png'))
except:
    error("Online Video Check Error!")
