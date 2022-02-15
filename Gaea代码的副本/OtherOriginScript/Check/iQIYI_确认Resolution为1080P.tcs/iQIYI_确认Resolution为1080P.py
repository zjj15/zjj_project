from autost.api import *
touch_if(Template("../../Design/OnlineVideo_Login_cancel.png"), timeout=1)
try:
    assert_exists(Template('../../Design/OnlineVideo_Resolution_720P.png'))
except:
    error('OnlineVideo Resolution 720P Check Error!')
