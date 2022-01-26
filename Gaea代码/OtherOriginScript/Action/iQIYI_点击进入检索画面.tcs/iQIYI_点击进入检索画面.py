from autost.api import *

touch_if(Template('../../Design/OnlineVideo_Agreement_Confirm.png'), timeout=3)
touch_if(Template("../../Design/OnlineVideo_Login_cancel.png"), timeout=1)
touch_if(Template('../../Design/OnlineVideo_PlayScreen_return.png'), timeout=3)
touch_if(Template('../../Design/OnlineVideo_PlayScreen_return.png'), timeout=3)
touch(Template('../../Design/OnlineVideo_Screen_Srch.png'))

touch(Template('../../Design/OnlineVideo_InputBox_Srch.png'))
try:
    assert_exists(Template('../../Design/IME_BTPhone_keyboard_icon.png'))
except:
    error('OnlineVideo enter search screen Error!')
