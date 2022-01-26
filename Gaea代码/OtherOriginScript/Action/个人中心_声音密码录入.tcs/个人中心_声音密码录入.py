from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print("__脚本名称: " + __file__)

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

for _ in range(5):
    touch_if(Template('../../Design/个人中心_声音登switch_off.png'), timeout=2)
    if poco('开启声音登录', text='开启声音登录', timeout=1.2).exists():
        say(Audio('../../Design/Audios/你好英菲.wav'))
        continue
    if poco('已录入成功！', text='已录入成功！', timeout=1).exists():
        poco('完成', text='完成').click()
        break
    if exists(Template('../../Design/个人中心_声音登switch_on.png'), timeout=2):
        break
else:
    error(__file__+' error')