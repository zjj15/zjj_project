from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
#DEV2 = 'iAndroid://127.0.0.1:5037/031603b3f8141501'
DEV2 = 'iAndroid://127.0.0.1:5037/DRGGAM0860501882'
CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
print("__脚本名称: " + __file__)
if exists(Template('../../../Design/statusbar_bt_mark.png'), timeout=3, device=DEV1):
    pass
else:
 
    do_segment(Segment('../../../Common/Phone_A_MB_0107/enter_btsetting.tcs'))
    #do_segment(Segment('../../../Common/Phone_S_MB_0569/enter_btsetting.tcs'))

    touch_if(Template('../../../Design/Phone_A_MB_0107/bt_switch_off.png'), timeout=2, device=DEV2)


    if exists(Template('../../../Design/BT_MSG_connected.png'), timeout=10, device=DEV1):
        pass
    else:    
        do_segment(Segment('../../BT_连接断连手机.tcs'))
        #touch_if(Template('../../../Design/bt_device_SMB0569.png'), timeout=5, device=DEV1)
    #assert_exists(Template('../../../Design/bt_SMB0569_connected.png'), timeout=60, device=DEV1)

 
