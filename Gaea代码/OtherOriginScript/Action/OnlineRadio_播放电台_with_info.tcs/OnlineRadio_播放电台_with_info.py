from autost.api import *
## 喜马拉雅app
DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print('__脚本名称: ' + __file__)

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

do_segment(Segment('../../Screen/迁移到Nissan Radio画面.tcs'))

def refresh():
    for _ in range(5):
        if poco('刷新重试', text='刷新重试', timeout=5).exists():
            poco('刷新重试', text='刷新重试').click()
        else:
            break

def play_audio():
    for _ in range(2):
        touch_if(Template('../../Design/ximalaya_back_icon.png'), timeout=1.5)
        sleep(2)

    poco('首页', text='首页').click()
    program_cover_title = poco(resourceId='com.ximalaya.ting.android.car:id/tv_cover_title1', pos2=[261, 508]).get_attr('text')
    #program_name = poco(resourceId='com.ximalaya.ting.android.car:id/tv_title', pos2=[235, 480]).get_attr('text')
    if program_cover_title:
        poco(resourceId='com.ximalaya.ting.android.car:id/tv_cover_title1', pos2=[261, 508]).click()
        poco(resourceId='com.ximalaya.ting.android.car:id/tv_track_title', pos2=[285, 561]).click()
        refresh()
        #防止是第一个
        keyevent(PRESET_SEEK_UP)
        touch_if(Template('../../Design/ximalaya_pause_icon.png'), timeout=3)
        touch_if(Template('../../Design/ximalaya_pause_icon.png'), timeout=3)
    else:
        error('wifi 信号不良')
    assert_exists(Template('../../Design/ximalaya_playing_icon.png'))

refresh()
try:
    play_audio()
    sleep(2)
    ## 控件树获取节目名
    #resourceId:        com.ximalaya.ting.android.car:id/title
    ST.OnlineRadio_program_name = poco(className='android.widget.TextView', pos2=[507, 221] ).get_attr('text')
    print('ST.OnlineRadio_program_name：', ST.OnlineRadio_program_name)
except:
    error('__脚本名称: ' + __file__+ 'Check error')
finally:
    #record previous/next program name
    #上一首
    keyevent(PRESET_SEEK_DOWN)
    sleep(1)
    ## 控件树获取节目名
    ST.OnlineRadio_program_previous = poco(className='android.widget.TextView', pos2=[507, 221] ).get_attr('text')
    #下一首
    keyevent(PRESET_SEEK_UP)
    sleep(1)
    keyevent(PRESET_SEEK_UP)
    sleep(1)
    ## 控件树获取节目名
    ST.OnlineRadio_program_next = poco(className='android.widget.TextView', pos2=[507, 221] ).get_attr('text')
    keyevent(PRESET_SEEK_DOWN)
    sleep(1)
    print('ST.OnlineRadio_program_previous: '+ST.OnlineRadio_program_previous)
    print('ST.OnlineRadio_program_name: '+ST.OnlineRadio_program_name)
    print('ST.OnlineRadio_program_next: '+ST.OnlineRadio_program_next)
