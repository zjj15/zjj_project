from autost.api import *
DEV1 = ST.DEV1

#前置条件
##打开USB端口
do_segment(Segment('../../Action/USB_端口1ON.tcs'))
CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

do_segment(Segment('../迁移到在线视频画面.tcs'))
touch_if(Template("../../Design/Login_Skip.png"), timeout=2)
##画面迁移到USB Video画面
poco('USB视频', text='USB视频', timeout=10).click()
try:
    assert_exists(Template('../../Design/VideoPicture_USB_Video_button_focus.png'))

except:
    error('IntoUSBVideo  Error!')
