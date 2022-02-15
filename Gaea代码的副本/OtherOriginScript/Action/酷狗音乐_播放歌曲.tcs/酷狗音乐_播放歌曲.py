from autost.api import *


#touch_if(Template('../../Design/OnlienMusic_Agreement_agree.png'), timeout=2)

#touch([235, 631])
#touch([457, 274])
ST.OnlineMusic_song_name = None
touch_if(Template('../../Design/OnlineMusic_NetworkError.png'), timeout=3)


def play_first_song_list():
    touch_if(Template('../../Design/KuGou_songlist_back.png'), timeout=2)
    if poco(className='android.widget.TextView', pos2=[181, 637]).exists():
        poco(className='android.widget.TextView', pos2=[181, 637]).click()
    for _ in range(30):
        if poco('拼命加载中，请稍后', text='拼命加载中，请稍后', timeout=1.5).exists():
            sleep(1)
        else:
            break
    poco('播放全部', text='播放全部').click()
    sleep(3)

def play_second_song_list():
    touch_if(Template('../../Design/KuGou_songlist_back.png'), timeout=2)
    poco(className='android.widget.TextView', pos2=[385, 637]).click()
    for _ in range(30):
        if poco('拼命加载中，请稍后', text='拼命加载中，请稍后', timeout=1.5).exists():
            sleep(1)
        else:
            break
    poco('播放全部', text='播放全部').click()
    sleep(3)

play_first_song_list()
for i in range(30):
    if exists(Template('../../Design/OnlienMusic_Play_Button.png'), timeout=1):
        break
    if exists(Template('pic/capture_20210506145326162694.png'), timeout=1):#new
        break
else:
    play_second_song_list()

for i in range(20):
    if exists(Template('../../Design/KuGou_vip_song_icon.png'), timeout=1.5):
        swipe([837,644],[837,369])
        sleep(1)
    else:
        print('start to play')
        touch([470, 388])
        if exists(Template('pic/capture_20210506145326162694.png'), timeout=30):#new
            break
        if poco('知道了', text='知道了', timeout=1.5).exists():
            poco('知道了', text='知道了', timeout=1.5).click()
            play_second_song_list()
        else:
            break
    if 10==i:
        play_second_song_list()
    if poco('知道了', text='知道了', timeout=1.5).exists():
        poco('知道了', text='知道了', timeout=1.5).click()
        play_second_song_list()

ST.OnlineMusic_song_name = poco(className='android.widget.TextView', pos2=[1540, 177] ).get_attr('text')
pos2_x, pos2_y = poco(className='android.widget.TextView', text=ST.OnlineMusic_song_name).get_attr('pos2')

ST.OnlineMusic_song_previous = poco(className='android.widget.TextView', pos2=[pos2_x, pos2_y-100] ).get_attr('text')
ST.OnlineMusic_song_next = poco(className='android.widget.TextView', pos2=[pos2_x, pos2_y+100] ).get_attr('text')
print('cur song name：', ST.OnlineMusic_song_name)
print('previous song name：', ST.OnlineMusic_song_previous)
print('next song name：', ST.OnlineMusic_song_next)


for i in range(30):
    if exists(Template('../../Design/OnlienMusic_Play_Button.png'), timeout=1):
        break
    if exists(Template('pic/capture_20210506145326162694.png'), timeout=1):#new
        break
else:
    error('OnlineMusic Play Error!')


