from autost.api import *
touch_if(Template('../../Design/OnlineVideo_Login_cancel.png'), timeout=1)
touch_if(Template('../../Design/OnlineVideo_Agreement_Confirm.png'), timeout=2)
touch_if(Template('../../Design/OnlineVideo_return_icon.png'), timeout=2)

touch(Template('../../Design/OnlineVideo_Screen_Srch.png'))

try:
    assert_exists(Template('../../Design/OnlienVideo_RecentSearch_empty.png'))
except:
    error('Online Video Recent Search init Check Error!')
