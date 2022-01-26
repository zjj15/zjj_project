from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print('__脚本名称: ' + __file__)

def enter_screen_KTV():
    flick_to(Template('../../../../Design/InCarKTV_Card.png'), [968, 342], DIR_LEFT, step=1, speed=SPEED_NORMAL)
    sleep(1.5)
    touch(Template('../../../../Design/InCarKTV_Card.png'))
    for _ in range(100):
        if poco('com.changba.sd:id/iv_slogen', timeout=3).exists() or poco('com.changba.sd:id/iv_logo', timeout=3).exists():
            sleep(1)
        else:
            break
    touch_if(Template('../../../../Design/InCarKTV_checkbox.png'), timeout=3)
    touch_if(Template('../../../../Design/InCarKTV_agree.png'), timeout=3)

# case suffix:0001
do_segment(Segment('../../../../Common/BackHomeView.tcs'))
try:
    assert_exists(Template('../../../../Design/statusbar_ktv_unselected.png'), threshold=0.90, device=DEV1)
    enter_screen_KTV()
    poco('为了您的驾驶安全，请勿在车辆行驶过程中K歌。', text='为了您的驾驶安全，请勿在车辆行驶过程中K歌。').assert_exists()
    poco('安全提示', text='安全提示').assert_exists()
except:
    error('__脚本名称: ' + __file__+ 'Check error')