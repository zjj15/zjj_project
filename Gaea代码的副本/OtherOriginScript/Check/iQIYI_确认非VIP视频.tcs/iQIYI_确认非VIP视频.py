from autost.api import *

touch_if(Template("../../Design/OnlineVideo_Login_cancel.png"), timeout=1)
if exists(Template('../../Design/OnlineVideo_vip_icon.png'), timeout=3) or exists(Template('../../Design/OnlineVideo_vip_icon_big.png'), timeout=3):
    error('OnlineVideo not VIP mark Check Error!')
else:
    pass
