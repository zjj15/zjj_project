from autost.api import *
#播放听书内容，保证时间长点
DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print('__脚本名称: ' + __file__)

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
ST.OnlineRadio_program_name = None

for i in range(2):
    if poco(text='').exists():
        poco(text='').click()
poco(text='首页').click()
poco(text='推荐').click()    


touch_if(Template('../../Design/ximalaya_pause_base1.png'), timeout=3)
touch_if(Template('../../Design/ximalaya_pause_base1.png'), timeout=3)

try:
    assert_exists(Template('../../Design/ximalaya_playing_base_1.png'))
    #防止是第一个
    keyevent(WIRECTR_TRACK_UP)
    sleep(2)
    ST.OnlineRadio_program_name = poco(className='android.widget.TextView', pos2=[681, 627] ).get_attr('text')
    print('ST.OnlineRadio_program_name：', ST.OnlineRadio_program_name)
except:
    error('__脚本名称: ' + __file__+ 'Check error')
finally:
    #record previous/next program name
    #WIRECTR_TRACK_DOWN：上一首
    keyevent(WIRECTR_TRACK_DOWN)
    sleep(1)
    ST.OnlineRadio_program_previous = poco(className='android.widget.TextView', pos2=[681, 627] ).get_attr('text')
    #WIRECTR_TRACK_DOWN：下一首
    keyevent(WIRECTR_TRACK_UP)
    sleep(1)
    keyevent(WIRECTR_TRACK_UP)
    sleep(1)
    ST.OnlineRadio_program_next = poco(className='android.widget.TextView', pos2=[681, 627] ).get_attr('text')
    keyevent(WIRECTR_TRACK_DOWN)
    sleep(1)
    print('ST.OnlineRadio_program_previous: '+ST.OnlineRadio_program_previous)
    print('ST.OnlineRadio_program_name: '+ST.OnlineRadio_program_name)
    print('ST.OnlineRadio_program_next: '+ST.OnlineRadio_program_next)
