from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
DEV2 = 'iAndroid://127.0.0.1:5037/031603b3f8141501'

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

print("__脚本名称: " + __file__)
#1、System MSG: Initialize waiting message
#touch(Template('../../Design/Setting_Factory_Reset_ok.png'), timeout=1, device=DEV1)
#2、割入incoming call：手机2拨打车机电话_仅呼叫

try:
    touch_if(Template('../../Design/Phone_S_MB_0569/Diag_CallBegin.png'), device=DEV2, threshold=0.95)
    touch(Template('../../Design/Setting_Factory_Reset_ok.png'), timeout=1, device=DEV1)
    touch_if(Template('../../Design/BTHF_HU_hangup.png'), timeout=2, device=DEV1)
    if exists(Template('../../Design/Setting_Factory_Reset_Success.png'), timeout=15):
        pass
    else:
        error('Check_BT电话画面 error...')
finally:
    do_segment(Segment('../../../Action/Message/手机2挂断电话.tcs'))

