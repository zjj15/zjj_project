from autost.api import *

touch_if(Template('../../../Design/OnlineVideo_Agreement_Confirm.png'), timeout=2)
touch_if(Template('../../../Design/个人中心_实名认证_X.png'), timeout=2)
for _ in range(3):
    touch_if(Template('../../../Design/OnlineVideo_Screen_Srch.png'), timeout=2)
    sleep(0.5)

try:
    poco(text='yi').assert_exists()
except:
    error('OnlineVideo Recent Search Error!')
