from autost.api import *

DEV1="Gaea://127.0.0.1:5037/GFEDCBA0987654321"
#登录状态
print('__脚本名称: ' + __file__)


for i in range(3):
    do_segment(Segment('../../Common/BackHomeView.tcs'))
    flick_to(Template('../../Design/iCar_Card.png'), [970, 367], DIR_LEFT, step=1, speed=SPEED_NORMAL)
    sleep(1)
    touch(Template('../../Design/iCar_Card.png'), timeout=5)
    for _ in range(4):
        if poco('允许', text='允许', timeout=1).exists():
            poco('允许', text='允许').click()
 
    touch_if(Template('../../Design/车联服务画面.png'))
    if poco(text='2G季包').exists():
        poco('com.szlanyou.usercenter:id/iv_cancel').click()
        poco(text='车联服务').click()
    touch_if(Template('../../Design/车联服务画面.png'))    
 
    if exists(Template('../../Design/个人中心_账号mark.png'),device=DEV1,timeout=5):
        break
    if exists(Template('../../Design/个人中心_实名认证.png'), timeout=5, threshold=0.95):
        wait_for_appearance(Template('../../Design/个人中心_实名认证_X.png'), timeout=5)
        do_segment(Segment('../../Action/设定时间同步.tcs'))
        sleep(10)
        touch_if(Template('../../Design/个人中心_实名认证_X.png'), timeout=5)
        continue
    if exists(Template('../../Design/Login_Skip.png'), timeout=2) or poco('登录', text='登录', timeout=2).exists():
        do_segment(Segment('../../Action/设定时间同步.tcs'))
        do_segment(Segment('../../Action/个人中心登录_账号1.tcs'))
        continue
# current version can not into iCar_Card(20210429)
try:
    assert_exists(Template('../../Design/个人中心_账号mark.png'),device=DEV1,timeout=5) 
except:
    error('Into iCar Error!')
