from autost.api import *
#P42Q车系：等同Steering wheel Switch面板的seekup/down

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print("__脚本名称: " + __file__)

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

key_name = get_param('keyname')
if key_name:
    key_name_lower = key_name.lower()
else:
    key_name_lower = ''

if 'seekup' == key_name_lower:
    keyevent(SEEK_UP, panel='Preset Switch', mode='CAN', channel=CANBUS_CH1)
    #keyevent(SEEK_UP, panel='Steering Control Switch', mode='CAN', channel=CANBUS_CH1)
elif 'seekdown' == key_name_lower:
    keyevent(SEEK_DOWN, panel='Preset Switch', mode='CAN', channel=CANBUS_CH1)
    #keyevent(SEEK_DOWN, panel='Steering Control Switch', mode='CAN', channel=CANBUS_CH1)
else:
    error('invalid param')

