from autost.api import *

touch_if(Template('../../Design/OnlineVideo_Agreement_Confirm.png'), timeout=3)
touch_if(Template('../../Design/OnlineVideo_Login_cancel.png'), timeout=1)
touch_if(Template('../../Design/OnlineVideo_PlayScreen_return.png'), timeout=3)
touch_if(Template('../../Design/OnlineVideo_PlayScreen_return.png'), timeout=3)

touch(Template('../../Design/OnlineVideo_Screen_Srch.png'))

touch(Template('../../Design/OnlineVideo_InputBox_Srch.png'))

key_words = get_param('keywords')
print('get_param: key_words:',key_words)
if 'yi' == key_words:
    touch(Template('../../Design/OnlineVideo_SrchKeyboard_y.png'),threshold = 0.8)
    touch(Template('../../Design/OnlineVideo_SrchKeyboard_i.png'),threshold = 0.8)
    for i in range(2):
        touch(Template('../../Design/OnlineVideo_SrchKeyboard_confirm.png'),threshold = 0.8)
elif 'yyyyy' == key_words:
    for i in range(5):
        touch(Template('../../Design/OnlineVideo_SrchKeyboard_y.png'),threshold = 0.8)
    for i in range(2):
        touch(Template('../../Design/OnlineVideo_SrchKeyboard_confirm.png'),threshold = 0.8)
else:
    error('invalid param')
