from autost.api import *
DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
print("__脚本名称: " + __file__)


if exists(Template('../../Design/ShortBar_Setting_nofocus.png'), timeout=2, threshold=0.90, device=DEV1) or exists(Template('../../Design/ShortBar_SettingCentral_focus.png'), timeout=2, device=DEV1, threshold=0.90):
    pass
else:
    do_segment(Segment('../迁移到中控设定画面.tcs'))    
touch([61, 455], device=DEV1)
touch([61, 455], device=DEV1)
touch([242, 149], device=DEV1)
