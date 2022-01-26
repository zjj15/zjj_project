from autost.api import *

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

## if test case contains IQIYI
## 机能开发不全
## 爱奇艺必须在账号登录下测试
## pass
##end

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
#车型：P42Q
#账号：88820212011
#密码：Abc123456！

do_segment(Segment('../../Screen/迁移到个人中心画面.tcs'))
sleep(12)
for _ in range(4):
    if exists(Template('../../Design/Login_Skip.png'), timeout=2) or poco('登录', text='登录', timeout=2).exists():
        if poco('点击按钮后，请按提示操作', text='点击按钮后，请按提示操作', timeout=1.5).exists():
            poco(text='换个方式登录').click()
            poco('密码登录', text='密码登录').click()
        break
    if exists(Template('../../Design/个人中心_账号mark.png'),device=DEV1,timeout=10):
        poco('账号', text='账号').click()
        if poco('退出', text='退出', timeout=3).exists():
            poco('退出', text='退出').click()
            poco('坚持退出', text='坚持退出').click()
        if poco('立即登录', text='立即登录', timeout=3).exists():
            poco('立即登录', text='立即登录').click()
        sleep(8)
    if poco('账号设置', text='账号设置', timeout=2).exists():
        poco('账号设置', text='账号设置', timeout=2).click()
    if exists(Template('../../Design/个人中心_实名认证.png'), timeout=5, threshold=0.95):
        wait_for_appearance(Template('../../Design/个人中心_实名认证_X.png'), timeout=5)
        do_segment(Segment('../设定时间同步.tcs'))
        sleep(10)
        touch_if(Template('../../Design/个人中心_实名认证_X.png'), timeout=5)
        do_segment(Segment('../../Screen/迁移到个人中心画面.tcs'))
        sleep(12)
        continue
