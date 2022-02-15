from autost.api import *
touch_if(Template('../../Design/OnlineVideo_Login_cancel.png'), timeout=1)
for i in range(6):
    if poco(text='高清 画质切换中，请稍后…').exists():
        sleep(10)
    else:
        break

assert_exists(Template('../../Design/OnlineVideo_Resolution_High.png'))

