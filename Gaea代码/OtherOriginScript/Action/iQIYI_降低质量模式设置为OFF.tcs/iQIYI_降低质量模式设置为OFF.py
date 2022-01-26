from autost.api import *

touch_if(Template('../../Design/OnlineVideo_Login_cancel.png'), timeout=1)


if exists(Template('../../Design/OnlineVideo_BitStreamQualit_icon.png')) :
    touch_if(Template('../../Design/OnlineVideo_BitStreamQualit_On_icon.png'), timeout=2)
else:
    touch([289, 599])
    touch_if(Template('../../Design/OnlineVideo_BitStreamQualit_On_icon.png'), timeout=2)
try:
    assert_exists(Template('../../Design/OnlineVideo_BitStreamQualit_icon.png'))
    assert_exists(Template('../../Design/OnlineVideo_BitStreamQualit_Off_icon.png'))
except:
    error('Setting NetQuality Error!')
