from autost.api import *
touch_if(Template('../../Design/OnlineVideo_Login_cancel.png'), timeout=1)
try:
    assert_exists(Template('../../Design/SkipHeaderTailer_ON.png'), threshold=0.88)
except:
    error('SkipHeaderTailer ON Check Error!')
