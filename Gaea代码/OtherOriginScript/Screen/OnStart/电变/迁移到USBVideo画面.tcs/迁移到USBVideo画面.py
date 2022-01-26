from autost.api import *
DEV1 = ST.DEV1

#前置条件
##打开USB端口
do_segment(Segment('../../../../Action/USB_端口1ON.tcs'))
# IG OFF
pwt_stop()
pwt_send(pwt_file='./waves/IG_OFF.pwt')
pwt_standby(mode=0x111)
pwt_play()
while pwt_state(wait=1) == 'play':
    print("Tbox PWT wave playing...")
print('Tbox PWT wave playing END!')

##画面迁移到USB Video画面
do_segment(Segment('../../../../Common/BackHomeView.tcs'))

flick_to(Template('../../../../Design/VideoPicture_Card.png'), [1904, 333], DIR_LEFT)
sleep(1)
touch(Template('../../../../Design/VideoPicture_Card.png'))

for _ in range(3):
    touch_if(Template('../../../../Design/OnlineVideo_Login_cancel.png'), timeout=2)
    touch_if(Template('../../../../Design/OnlineVideo_jump_icon.png'), timeout=2)
    if poco('USB视频', text='USB视频', timeout=5).exists():
        break
    if poco('爱奇艺账号登录', text='爱奇艺账号登录', timeout=10).exists():
        do_segment(Segment('../../../../Action/iQIYI_登录二维码画面close键押下.tcs'))

poco('USB视频', text='USB视频', timeout=10).click()
try:
    assert_exists(Template('../../../../Design/VideoPicture_USB_Video_button_focus.png'))

except:
    error('IntoUSBVideo  Error!')
