from autost.api import *
DEV = ST.DEV1

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

#前置条件
##打开USB端口
#do_segment(Segment('../../Common/打开素材U盘.tcs'))
do_segment(Segment('../../Action/USB_端口1ON.tcs'))
if exists(Template('../../Design/Music_USBAudio_btn_focus.png'), timeout=1):
    pass
elif exists(Template('../../Design/Music_USBAudio_btn_nofocus.png'), timeout=1, threshold=0.85) or exists(Template('../../Design/Music_USBAudio_btn_nofocus_BK_KuGou.png'), timeout=1, threshold=0.85):
    touch_if(Template('../../Design/Music_USBAudio_btn_nofocus.png'), timeout=1,threshold=0.85)
    #touch一次坐标
    touch([78, 396])
    touch_if(Template('../../Design/Music_USBAudio_btn_nofocus_BK_KuGou.png'), timeout=1,threshold=0.85)
else:
    #画面迁移到USB Audio画面
    do_segment(Segment('../../Common/BackHomeView.tcs'))
 
    flick_to(Template('../../Design/Music_Card.png'), [971, 353], DIR_LEFT, step=1, speed=SPEED_NORMAL)
    sleep(1)
    if exists(Template('../../Design/Music_USBAudio_btn_focus.png'), timeout=2):
        pass
    else:
        for i in range(3):
            touch_if(Template('../../Design/Music_Card.png'), timeout=1)
            touch_if(Template('../../Design/Music_USBAudio_btn_nofocus.png'), timeout=2,threshold=0.85)
            if exists(Template('../../Design/Music_USBAudio_btn_focus.png'), timeout=1):
                break
try:
    assert_exists(Template('../../Design/Music_USBAudio_btn_focus.png'))

except:
    error('IntoUSBAudio Error!')

