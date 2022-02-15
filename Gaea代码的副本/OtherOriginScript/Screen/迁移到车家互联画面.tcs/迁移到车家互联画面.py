from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

print('__脚本名称: ' + __file__)

do_segment(Segment('../../Common/BackHomeView.tcs'))

flick_to(Template('../../Design/SmartHome_Card.png'), [968, 342], DIR_LEFT, step=1, speed=SPEED_NORMAL,device=DEV1)

touch(Template('../../Design/SmartHome_Card.png'),device=DEV1)
if exists(Template('../../Design/系统MSG_系统时间不一致.png'), timeout=2):
    do_segment(Segment('../../Action/设定时间同步.tcs'))

'''
for i in range(3):
    if exists(Template('../../Design/SmartHome_Reconnect_Tip.png'),device=DEV1):
        touch(Template('../../Design/SmartHome_Reconnect_Tip.png'),device=DEV1)
        sleep(3)
if exists(Template('../../Design/车家互联_引导协议.png'), timeout=2):
    poco(text='同意').click()
    wait_for_disappearance(Template('../../Design/车家互联_连接中MSG.png'))

#poco(text='登录').assert_exists()
assert_exists(Template('../../Design/车家互联图标.png'))




#目前没有账户，只能进到登录账户页面
'''

if poco(text='推荐使用英菲智联APP扫码自动登录').exists():
    print('车家互联未登录')



