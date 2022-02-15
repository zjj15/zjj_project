from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
DEV2 = 'iAndroid://127.0.0.1:5037/031603b3f8141501'

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
print("__脚本名称: " + __file__)
#1、点击开始搜索按钮：ModeinMSG_电台搜索中_显示
poco('开始搜索', text='开始搜索').click()
#2、割入：短押HardKey_TrackUP
keyevent(WIRECTR_TRACK_UP, device=DEV1)
#3、Check_无收藏电台_电台搜索中
assert_exists(Template('../../../Design/MSG_noFavorite_on_searching.png'), device=DEV1)
