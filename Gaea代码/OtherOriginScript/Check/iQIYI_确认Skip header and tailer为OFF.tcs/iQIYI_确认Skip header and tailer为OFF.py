from autost.api import *
touch_if(Template("../../Design/OnlineVideo_Login_cancel.png"), timeout=1)
try:
    assert_exists(Template('../../Design/SkipHeaderTailer_OFF.png'))
except:
    error('SkipHeaderTailer OFF Check Error!')
