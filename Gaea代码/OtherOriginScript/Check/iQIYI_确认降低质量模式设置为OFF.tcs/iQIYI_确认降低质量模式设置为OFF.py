from autost.api import *
touch_if(Template('../../Design/OnlineVideo_Login_cancel.png'), timeout=1)
if exists(Template('../../Design/OnlineVideo_Resolution_High.png'), timeout=2):
    touch(Template('../../Design/OnlineVideo_Resolution_High.png'))
 
elif exists(Template('../../Design/OnlineVideo_Resolution_Standard.png'), timeout=2):
    touch(Template('../../Design/OnlineVideo_Resolution_Standard.png'))
 
elif exists(Template('../../Design/OnlineVideo_Resolution_720P.png'), timeout=2):
    touch(Template('../../Design/OnlineVideo_Resolution_720P.png'))
 
 
try:
    assert_exists(Template('../../Design/OnlineVideo_BitStreamQualit_Off_icon.png'))
    touch([321, 641])
except:
    error('OnlineVideo NetQuality Lower OFF Check Error!')
