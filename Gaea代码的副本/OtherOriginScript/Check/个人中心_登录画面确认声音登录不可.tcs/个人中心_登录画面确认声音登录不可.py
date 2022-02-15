from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print("__脚本名称: " + __file__)

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

poco('换个方式登录', text='换个方式登录').click()
poco('声音登录', text='声音登录').assert_exists()
poco('声音登录', text='声音登录').click()
if exists(Template("../../Design/个人中心_msg_声音登录不可.png"), threshold=0.96, timeout=5):
   sleep(3)
   pass
else:
    poco('登录', text='登录').assert_exists()