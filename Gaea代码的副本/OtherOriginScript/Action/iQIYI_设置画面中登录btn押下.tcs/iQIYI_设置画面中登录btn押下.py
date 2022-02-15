from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

do_segment(Segment('../../Screen/进入iQIYI设置画面.tcs'))
poco('登录', text='登录', package='com.iauto.onlinevideo').click()
for i in range(2):
    if poco('爱奇艺账号登录', text='爱奇艺账号登录', timeout=2).exists():
        break

#poco('android.widget.ImageView', pos2=[548, 160], org_size=(84, 84), package='com.iauto.systemview').click()
