from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print('__脚本名称: ' + __file__)

def enter_screen_usbvideo():
    flick_to(Template('../../../../Design/VideoPicture_Card.png'), [968, 342], DIR_LEFT, step=1, speed=SPEED_NORMAL)
    sleep(1.5)
    touch(Template('../../../../Design/VideoPicture_Card.png'))
    for _ in range(3):
        if poco('USB视频', text='USB视频', timeout=5).exists():
            break
        if poco('爱奇艺账号登录', text='爱奇艺账号登录', timeout=10).exists():
            do_segment(Segment("../../../../Action/iQIYI_登录二维码画面close键押下.tcs"))
    touch([75, 386])
    #poco('USB视频', text='USB视频', timeout=10).click()

# case suffix:0001
do_segment(Segment('../../../../Common/BackHomeView.tcs'))
try:
    assert_exists(Template('../../../../Design/statusbar_usbvideo.png'), threshold=0.90, device=DEV1)
    enter_screen_usbvideo()
    poco('为了您的驾驶安全，请勿在车辆行驶过程中观看视频。', text='为了您的驾驶安全，请勿在车辆行驶过程中观看视频。').assert_exists()
    poco('安全提示', text='安全提示').assert_exists()
except:
    error('__脚本名称: ' + __file__+ 'Check error')

