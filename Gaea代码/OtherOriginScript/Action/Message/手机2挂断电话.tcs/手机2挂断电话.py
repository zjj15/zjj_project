from autost.api import *

#Action
# 手机7：A_MB_0107　号码：17301643089　蓝牙连接车机　连接IDE
# 手机2：S_MB_0569　号码：17301641459 　连接IDE
# 手机3: A_MB_0087： 号码：


DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
#第一部拨号手机
DEV2 = 'iAndroid://127.0.0.1:5037/031603b3f8141501'#S-MB-0569
DEV7 = 'iAndroid://127.0.0.1:5037/DRGGAM0860501882'
DialNumber = '17301641459'
CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

for i in range(2):
    if exists(Template('../../../Design/Phone_S_MB_0569/BTCalling_hangup_1.png'), timeout=3, device=DEV2):
        touch(Template('../../../Design/Phone_S_MB_0569/BTCalling_hangup_1.png'), device=DEV2)
    elif exists(Template('../../../Design/Phone_S_MB_0569/BTCalling_statusbar.png'), timeout=2, device=DEV2):
        flick([528, 22], DIR_DOWN, step=20, speed=SPEED_NORMAL, device=DEV2)
        touch_if(Template('../../../Design/Phone_S_MB_0569/BTCalling_hangup_2.png'), timeout=5, device=DEV2)
        sleep(1)
        touch([666, 1256], device=DEV2)
    elif exists(Template('../../../Design/Phone_S_MB_0569/BTCalling_hangup_3.png'), timeout=2, device=DEV2):
        touch(Template('../../../Design/Phone_S_MB_0569/BTCalling_hangup_3.png'), device=DEV2)
        sleep(1)
    elif exists(Template('../../../Design/Phone_S_MB_0569/BTCalling_hangup_2.png'), timeout=5, device=DEV2):
        touch(Template('../../../Design/Phone_S_MB_0569/BTCalling_hangup_2.png'), timeout=5, device=DEV2)
    else:
        break

if exists(Template('../../../Design/BTHF_statusbar_EndCallBtn.png'), timeout=3, device=DEV1):
    wait_for_disappearance(Template('../../../Design/BTHF_statusbar_EndCallBtn.png'), timeout=100, device=DEV1)
