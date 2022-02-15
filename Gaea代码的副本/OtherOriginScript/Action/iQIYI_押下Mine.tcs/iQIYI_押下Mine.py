from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
touch_if(Template('../../Design/OnlineVideo_Login_cancel.png'), timeout=1)
touch_if(Template('../../Design/OnlineVideo_Agreement_Confirm.png'), timeout=3)

touch_if(Template('../../Design/OnlineVideo_PlayScreen_return.png'), timeout=3)
touch_if(Template('../../Design/OnlineVideo_PlayScreen_return.png'), timeout=3)

sleep(2)

# enter onlinevideo myfavorite
for i in range(3):
    if exists(Template('../../Design/OnlineVideo_Center.png'), timeout=2):
        touch(Template('../../Design/OnlineVideo_Center.png'),device=DEV1)

try:
    assert_exists(Template('../../Design/OnlineVideo_mine_icon.png'))
except:
    error('IQIYI 押下Mine: 进入我的页面失败')
