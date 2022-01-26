from autost.api import *

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

try:
    poco('跳过', text='跳过', package='com.szlanyou.usercenter').click()
except:
    print("跳过画面没有出现")
    pass
    