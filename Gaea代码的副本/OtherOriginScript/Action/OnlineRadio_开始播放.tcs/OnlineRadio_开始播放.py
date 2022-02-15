from autost.api import *
## 喜马拉雅app
DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print('__脚本名称: ' + __file__)

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
def refresh():
    for _ in range(5):
        if poco('刷新重试', text='刷新重试', timeout=5).exists():
            poco('刷新重试', text='刷新重试').click()
        else:
            break

def play_audio():
    for _ in range(2):
        touch_if(Template('../../Design/ximalaya_back_icon.png'), timeout=1.5)

    poco('首页', text='首页').click()
    program_cover_title = poco(resourceId='com.ximalaya.ting.android.car:id/tv_cover_title1', pos2=[261, 508]).get_attr('text')
    #program_name = poco(resourceId='com.ximalaya.ting.android.car:id/tv_title', pos2=[235, 480]).get_attr('text')
    if program_cover_title:
        poco(resourceId='com.ximalaya.ting.android.car:id/tv_cover_title1', pos2=[261, 508]).click()
        poco(resourceId='com.ximalaya.ting.android.car:id/tv_track_title', pos2=[249, 561]).click()
        refresh()
        touch_if(Template('../../Design/ximalaya_pause_icon.png'), timeout=3)
        touch_if(Template('../../Design/ximalaya_pause_icon.png'), timeout=3)
    else:
        error('wifi 信号不良')
    assert_exists(Template('../../Design/ximalaya_playing_icon.png'))

refresh()
for _  in range(3):
    touch_if(Template('../../Design/ximalaya_pause_icon.png'), timeout=3)
    if exists(Template('../../Design/ximalaya_playing_icon.png'), timeout=1):
        break
    elif exists(Template('../../Design/ximalaya_playing_base_1.png'), timeout=1):
        break
    elif exists(Template('../../Design/ximalaya_playing_base_2.png'), timeout=1):
        break
    else:
        play_audio()
