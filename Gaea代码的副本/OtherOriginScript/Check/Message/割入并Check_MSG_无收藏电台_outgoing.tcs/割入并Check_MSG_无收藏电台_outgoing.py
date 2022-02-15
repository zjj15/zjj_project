from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
DEV2 = 'iAndroid://127.0.0.1:5037/DRGGAM0860501882'#Phone_A_MB_0107

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
print("__脚本名称: " + __file__)

#1、短押TrackUP：MSG:无收藏电台
keyevent(SEEK_DOWN, panel='Steering Control Switch', mode='CAN', device=DEV1, channel=CANBUS_CH1)
#2、割入outgoing call：手机7拨打手机2_仅呼出
touch_if(Template('../../Design/Phone_A_MB_0107/Diag_CallBegin.png'), device=DEV2, threshold=0.95)
#3、Check_MSG_无收藏电台_outgoing
if exists(Template('../../Design/MSG_NoCollectionRadio.png'), timeout=10, device=DEV1):
    pass
else:
    error('割入并Check_MSG_无收藏电台 error...')
