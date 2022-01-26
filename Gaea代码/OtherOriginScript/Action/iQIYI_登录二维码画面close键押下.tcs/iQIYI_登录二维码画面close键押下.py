from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print("__脚本名称: " + __file__)

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

poco('android.widget.ImageView', pos2=[548, 160], org_size=(84, 84), package='com.iauto.systemview').click()