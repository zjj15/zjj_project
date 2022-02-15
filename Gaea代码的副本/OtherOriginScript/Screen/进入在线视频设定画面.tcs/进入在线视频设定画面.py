from autost.api import *

if exists(Template('../../Design/OnlineVideo_Center.png'), timeout=3):
    touch(Template('../../Design/OnlineVideo_Center.png'))
    touch_if(Template('../../Design/OnlineVideo_Setting_notfocus.png'), timeout=3)
else:
    error('Online Video Screen not display!')
 
try:
    assert_exists(Template('../../Design/OnlineVideo_Setting_Cache.png'))
    assert_exists(Template('../../Design/OnineVideo_Setting_focus.png'))
except:
    error('IntoOnlineVideo Setting Error!')
