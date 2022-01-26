from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
DEV2 = 'iAndroid://127.0.0.1:5037/031603b3f8141501'
DEV7 = 'iAndroid://127.0.0.1:5037/DRGGAM0860501882'

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

print("__脚本名称: " + __file__)
#1、System MSG: Initialize waiting message
#touch(Template('../../Design/Setting_Factory_Reset_ok.png'), timeout=1, device=DEV1)
#2、割入outcoming call：手机7拨打手机2_仅呼叫


touch(Template('../../Design/Phone_A_MB_0107/Diag_CallBegin.png'), device=DEV7, threshold=0.95)
touch(Template('../../Design/Setting_Factory_Reset_ok.png'), timeout=1, device=DEV1)
if exists(Template('../../Design/Setting_Factory_Reset_Success.png'), timeout=15):
    pass
else:
    error('Check_BT电话画面 error...')

 
