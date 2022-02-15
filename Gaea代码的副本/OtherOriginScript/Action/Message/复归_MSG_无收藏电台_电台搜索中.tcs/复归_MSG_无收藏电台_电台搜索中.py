from autost.api import *
DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
DEV2 = 'iAndroid://127.0.0.1:5037/031603b3f8141501'

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
print("__脚本名称: " + __file__)

if exists(Template('../../../Design/MSG_NoCollectionRadio.png'), timeout=2, device=DEV1):
    wait_for_disappearance(Template('../../../Design/MSG_NoCollectionRadio.png'), timeout=25, device=DEV1)

do_segment(Segment('../复归_MSG_电台搜索中.tcs'))

if poco('我的收藏', text='我的收藏', timeout=2, device=DEV1).exists():
    poco('android.widget.ImageView', pos=(0.1046875, 0.2111111111111111)).click()    
