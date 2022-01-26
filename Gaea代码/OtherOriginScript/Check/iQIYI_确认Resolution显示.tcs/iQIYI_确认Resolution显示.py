from autost.api import *
touch_if(Template('../../Design/OnlineVideo_Login_cancel.png'), timeout=1)
try:
    if exists(Template('../../Design/OnlineVideo_Resolution_High.png'), timeout=2):
        pass
    elif exists(Template('../../Design/OnlineVideo_Resolution_Standard.png'), timeout=2):
        pass
    elif exists(Template('../../Design/OnlineVideo_Resolution_720P.png'), timeout=2):
        pass
except:
    error('OnlineVideo Resolution Check Error!')
