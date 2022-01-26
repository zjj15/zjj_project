from autost.api import *

DEV1="Gaea://127.0.0.1:5037/GFEDCBA0987654321"
#仅迁移到个人中心画面
#登录状态不定
print('__脚本名称: ' + __file__)

for i in range(3):
    do_segment(Segment('../../Common/BackHomeView.tcs'))
    flick_to(Template('../../Design/iCar_Card.png'), [970, 367], DIR_LEFT, step=1, speed= SPEED_NORMAL)
    sleep(1)
    touch(Template('../../Design/iCar_Card.png'), timeout=5)
    for _ in range(4):
        if poco('允许', text='允许', timeout=1).exists():
            poco('允许', text='允许').click()
    if poco(text='2G季包').exists():
        poco('com.szlanyou.usercenter:id/iv_cancel').click()
        poco(text='车联服务').click()
    if exists(Template('../../Design/个人中心_账号mark.png'),device=DEV1,timeout=5):
        sleep(8)
        break
    if exists(Template('../../Design/个人中心_实名认证.png'), timeout=5, threshold=0.95):
        wait_for_appearance(Template('../../Design/个人中心_实名认证_X.png'), timeout=5)
        do_segment(Segment('../../Action/设定时间同步.tcs'))
        sleep(10)
        #touch_if(Template('../../Design/个人中心_实名认证_X.png'), timeout=5)
        if poco('com.szlanyou.usercenter:id/tv_back', timeout=5).exists():
            poco('com.szlanyou.usercenter:id/tv_back').click()
        continue
    if exists(Template('../../Design/Login_Skip.png'), timeout=2) or poco('登录', text='登录', timeout=2).exists():
        break
    if poco('账号设置', text='账号设置', timeout=2).exists():
        poco('账号设置', text='账号设置', timeout=2).click()
        if exists(Template('../../Design/个人中心_账号mark.png'),device=DEV1,timeout=10):
            break
    if poco('重新连接', text='重新连接', timeout=2).exists():
        poco('重新连接', text='重新连接').click()
        sleep(8)
sleep(5)
