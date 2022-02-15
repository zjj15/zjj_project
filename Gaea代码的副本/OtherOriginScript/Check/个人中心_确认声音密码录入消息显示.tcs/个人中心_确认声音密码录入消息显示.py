from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print("__脚本名称: " + __file__)

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

for _ in range(5):
    touch_if(Template("../../Design/个人中心_声音登switch_off.png"), timeout=2)
    if poco('com.szlanyou.usercenter:id/tv_voice').exists():
        break
    
    '''
    if poco('开启声音登录', text='开启声音登录', timeout=1.2).exists():
        sleep(10)
        break
    '''
else:
    error(__file__+' error')
