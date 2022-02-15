from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print('__脚本名称: ' + __file__)

# case suffix:0001
def enter_screen_iqiyi():
    for i in range(3):
        if exists(Template('../../../../Design/ShortBar_OnlineVideo_focus.png'), timeout=1, threshold=0.95) and exists(Template('../../../../Design/OnlineVideo_Center.png'), timeout=1, threshold=0.95):
            break
        else:
            do_segment(Segment('../../../../Common/BackHomeView.tcs'))
            flick_to(Template('../../../../Design/Video_Picture_Card.png'), [970, 367], DIR_LEFT, step=1, speed=SPEED_NORMAL)
            sleep(1)
            touch(Template('../../../../Design/Video_Picture_Card.png'), timeout=5)
            touch_if(Template('../../../../Design/OnlineVideo_Login_cancel.png'), timeout=1)
            touch_if(Template('../../../../Design/OnlineVideo_PlayScreen_return.png'),timeout=1, threshold=0.95)
            if exists(Template('../../../../Design/个人中心_实名认证.png'), timeout=5, threshold=0.95):
                wait_for_appearance(Template('../../../../Design/个人中心_实名认证_X.png'), timeout=5)
                do_segment(Segment('../../../../Action/设定时间同步.tcs'))
                sleep(10)
                touch_if(Template('../../../../Design/个人中心_实名认证_X.png'), timeout=5)
                continue
            if exists(Template('../../../../Design/Login_Skip.png'), timeout=2) or poco('登录', text='登录', timeout=2).exists():
                do_segment(Segment('../../../../Action/设定时间同步.tcs'))
                do_segment(Segment('../../../../Action/个人中心登录_账号1.tcs'))
                continue
            touch_if(Template('../../../../Design/OnlineVideo_Agreement_Confirm.png'), timeout=3)
            touch_if(Template('../../../../Design/OnlineVideo_Login_cancel.png'), timeout=1)
            #touch_if(Template('../../../../Design/Login_Skip.png'), timeout=2)
            #touch_if(Template('../../../../Design/OnlineVideo_Login_cancel.png'), timeout=1)
            if poco('在线视频', text='在线视频', timeout=2).exists():
                poco('在线视频', text='在线视频', timeout=4).click()
                touch_if(Template('../../../../Design/OnlineVideo_Agreement_Confirm.png'), timeout=3)
            touch_if(Template('../../../../Design/OnlineVideo_Login_cancel.png'), timeout=1)
            if poco('爱奇艺账号登录', text='爱奇艺账号登录', timeout=10).exists():
                poco('android.widget.ImageView', pos=(0.3072916666666667, 0.28055555555555556)).click()
            if exists(Template('../../../../Design/ShortBar_OnlineVideo_focus.png'), timeout=5, threshold=0.95):
                break

do_segment(Segment('../../../../Common/BackHomeView.tcs'))
try:
    assert_exists(Template('../../../../Design/statusbar_iqiyi.png'), threshold=0.90, device=DEV1)
    enter_screen_iqiyi()
    poco('为了您的驾驶安全，请勿在车辆行驶过程中观看视频。', text='为了您的驾驶安全，请勿在车辆行驶过程中观看视频。').assert_exists()
    poco('安全提示', text='安全提示').assert_exists()
except:
    error('__脚本名称: ' + __file__+ 'Check error')