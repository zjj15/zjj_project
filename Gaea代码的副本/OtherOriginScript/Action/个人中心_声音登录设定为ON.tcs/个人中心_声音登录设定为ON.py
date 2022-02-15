from autost.api import *

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

if poco('账号设置', text='账号设置', timeout=2).exists():
    pass
else:
    poco('账号', text='账号').click()
    poco('账号设置', text='账号设置', timeout=2).assert_exists()

touch_if(Template('../../Design/个人中心_声音登switch_off.png'), timeout=2)
if poco('开启声音登录', text='开启声音登录', timeout=4).exists():
    do_segment(Segment('../个人中心_声音密码录入.tcs'))
else:
    assert_exists(Template('../../Design/个人中心_声音登switch_on.png'))
