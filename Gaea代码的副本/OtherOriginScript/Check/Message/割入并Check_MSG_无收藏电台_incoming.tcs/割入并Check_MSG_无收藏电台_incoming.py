from autost.api import *
DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
DEV2 = 'iAndroid://127.0.0.1:5037/031603b3f8141501'

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
print("__脚本名称: " + __file__)
#2、割入incoming call：手机2拨打车机电话_仅呼出
touch_if(Template('../../Design/Phone_S_MB_0569/Diag_CallBegin.png'), device=DEV2, threshold=0.95)
sleep(3)
#1、短押TrackUP：MSG:无收藏电台
keyevent(SEEK_DOWN, panel='Steering Control Switch', mode='CAN', device=DEV1, channel=CANBUS_CH1)
if exists(Template('../../Design/BTHF_incoming_EndCallBtn.png'), timeout=10, device=DEV1):
    #手机2挂断电话
    touch_if(Template('../../Design/Phone_S_MB_0569/BTCalling_hangup_1.png'), device=DEV2)
    #3、Check_MSG_无收藏电台_incoming
    if exists(Template('../../Design/MSG_NoCollectionRadio.png'), timeout=10, device=DEV1):
        pass
    elif exists(Template('../../Design/radio_tab_favorite_NoCollectionRadio.png'), timeout=10, device=DEV1):
        pass
    else:
        error('割入并Check_MSG_无收藏电台 error...')

