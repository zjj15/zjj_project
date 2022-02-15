from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
DEV3 = 'iAndroid://127.0.0.1:5037/DRGGAM0860501882'

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

do_segment(Segment('../../../Screen/迁移到中控设定画面.tcs'))

do_segment(Segment('../../../Screen/进入蓝牙设定画面.tcs'))

if exists(Template('../../../Design/bt_device_A_MB_0107_connected.png'), device=DEV1, timeout=5, threshold=0.95):
    pass
else:
    #设定画面
    do_segment(Segment('../enter_btsetting.tcs'))
    #可能是开关没开断连
    if exists(Template('../../../Design/Phone_A_MB_0107/bt_switch_off.png'), device=DEV3, timeout=1):
        touch(Template('../../../Design/Phone_A_MB_0107/bt_switch_off.png'), device=DEV3, timeout=1)
        if exists(Template('../../../Design/BT_device_disconnect.png'), device=DEV1, timeout=1):
            touch_if(Template('../../../design/BT_device_disconnect.png'), timeout=5, device=DEV1)
            wait_for_appearance(Template('../../../design/BT_MSG_connected.png'), timeout=20, device=DEV1)
    if exists(Template('../../../Design/bt_device_A_MB_0107_connected.png'), device=DEV1, timeout=5, threshold=0.95):
        pass
    else:
        touch(Template('../../../Design/Phone_A_MB_0107/seting_pair_newdevice.png'), device=DEV3)


        do_segment(Segment('../../../Action/设定_蓝牙删除车机已连接设备.tcs'))

        do_segment(Segment('../../../Action/设定_BT连接检索.tcs'))

        touch(Template('../../../Design/bt_device_A_MB_0107.png'), device=DEV1, threshold=0.95)
        wait_for_appearance(Template('../../../Design/Phone_A_MB_0107/seting_pair_msg.png'), timeout=30, device=DEV3)
        touch_if(Template('pic/capture_20210422210631915481.png'), timeout=3, device=DEV3)
 
        touch(Template('../../../Design/Phone_A_MB_0107/seting_pair_btn.png'), device=DEV3)

        wait_for_appearance(Template('../../../Design/BT_MSG_connected.png'), device=DEV1, timeout=20)

        assert_exists(Template('../../../Design/bt_device_A_MB_0107_connected.png'), device=DEV1)



