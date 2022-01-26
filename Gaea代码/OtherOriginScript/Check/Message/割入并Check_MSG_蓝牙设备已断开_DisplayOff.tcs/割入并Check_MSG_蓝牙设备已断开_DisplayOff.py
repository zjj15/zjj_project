from autost.api import *
#
DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
#DEV2 = 'iAndroid://127.0.0.1:5037/031603b3f8141501'
DEV2 = 'iAndroid://127.0.0.1:5037/DRGGAM0860501882'

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
print("__脚本名称: " + __file__)

do_segment(Segment('../../../Common/Phone_A_MB_0107/enter_btsetting.tcs'))
#do_segment(Segment('../../../Common/Phone_S_MB_0569/enter_btsetting.tcs'))

if exists(Template('../../../Design/check_displayoff.png'), timeout=2, device=DEV1) and exists(Template('../../../Design/Phone_A_MB_0107/bt_switch_on.png'), timeout=5, device=DEV2):
    touch(Template('../../../Design/Phone_A_MB_0107/bt_switch_on.png'), timeout=5, device=DEV2)
 
    #assert_exists(Template('../../../Design/Phone_A_MB_0107/bt_switch_off_status.png'), device=DEV2)
 
    sleep(2)
    assert_exists(Template('../../../Design/check_displayoff.png'), timeout=1, device=DEV1)
    touch([572, 37], device=DEV1)# do_segment(Segment('../../../Action/DisplayOff解除.tcs'))
    assert_not_exists(Template('../../../Design/statusbar_bt_mark.png'), timeout=3, device=DEV1)
    #if exists(Template('../../../Design/bt_device_A_MB_0107_connected.png'), device=DEV1, timeout=3) or exists(Template('../../../Design/check_BTconnecting.png'), device=DEV1, timeout=3):
    #    pass
    #else:
    #    error('割入并Check_MSG_蓝牙设备已断开_DisplayOff error')
