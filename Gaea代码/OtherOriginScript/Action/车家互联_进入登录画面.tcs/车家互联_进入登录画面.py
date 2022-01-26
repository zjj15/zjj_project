from autost.api import *

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
#车型：P42Q


if poco('请输入手机号码', text='请输入手机号码').exists():
    poco('请输入手机号码', text='请输入手机号码').click()
if poco(text='车家互联').exists():
    print('车家互联已登录')

