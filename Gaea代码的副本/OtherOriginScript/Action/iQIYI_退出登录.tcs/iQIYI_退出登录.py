from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

CANBUS_CH1 = 'MCAN'
CANBUS_CH2 = 'VCAN'
do_segment(Segment('../../Screen/迁移到在线视频画面.tcs'))
if exists(Template('../../Design/OnlineVideo_走形规制_安全提示MSG.png'),threshold = 0.95, timeout = 2):
    do_segment(Segment('../CAN_发送PKB_ON.tcs'))
do_segment(Segment('../iQIYI_押下Mine.tcs'))

touch_if(Template('../../Design/OnlineVideo_mine_setting_icon.png'),timeout=3,device=DEV1)
sleep(2)
touch_if(Template('../../Design/OnlineVideo_mine_setting_logOut_icon.png'),timeout=3,device=DEV1)
sleep(2)
touch_if(Template('../../Design/OnlineVideo_mine_setting_logout_yes.png'),timeout=3,device=DEV1)
