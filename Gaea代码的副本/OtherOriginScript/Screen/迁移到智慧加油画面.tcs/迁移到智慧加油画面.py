from autost.api import *

DEV1="Gaea://127.0.0.1:5037/GFEDCBA0987654321"

do_segment(Segment('../../Common/BackHomeView.tcs'))
swipe([1416, 325],[505, 345],device=DEV1)
sleep(2)

touch(Template('../../Design/SmartFuel_Card.png'),device=DEV1)
for _ in range(4):
    if poco('允许', text='允许', timeout=1).exists():
        poco('允许', text='允许').click()
    else:
        break
# current version can not into SmartFuel_Card(20210429)
touch_if(Template('../../Design/加油智慧_协议_同意btn.png'),device=DEV1,timeout=5)
if poco(text='您的爱车使用几号汽油?').exists():
    poco(text='确定').click()
if poco(text='去登录').exists():
    poco(text='去登录').click()
if poco('com.szlanyou.usercenter:id/iv_login_way_icon').exists():
    poco(text='换个方式登录').click()
    poco(text='密码登录').click()

try:
    assert_not_exists(Template('../../Design/SmartFuel_Card.png'),device=DEV1,timeout=5) 
except:
    error('Into theme shop Error!')
