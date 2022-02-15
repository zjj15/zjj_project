from autost.api import *
#要求当前只有一个连接
DEV1=ST.DEV1

do_segment(Segment('../../Screen/迁移到中控设定画面.tcs'))
do_segment(Segment('../../Screen/进入蓝牙设定画面.tcs'))
if exists(Template('../../design/BT_device_disconnect.png'), timeout=5, device=DEV1):
    touch(Template('../../design/BT_device_disconnect.png'), timeout=5, device=DEV1)
    wait_for_appearance(Template('../../design/BT_MSG_connected.png'), timeout=20, device=DEV1)