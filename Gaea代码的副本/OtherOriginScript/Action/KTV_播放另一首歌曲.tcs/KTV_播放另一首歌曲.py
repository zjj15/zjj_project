from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print("__脚本名称: " + __file__)

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
def play_another_song():
    for i in range(10):
        cur_song_name = poco(resourceId='com.changba.sd:id/playing_songinfo_tiny_song').get_attr('text')
        print('ST.KTV_song_name: ',ST.KTV_song_name)
        print('cur_song_name: ',cur_song_name)
        if exists(Template('../../Design/KTV_playing_btn.png')) and ST.KTV_song_name != cur_song_name:
            break
        elif exists(Template('../../Design/KTV_playing_btn.png')) and ST.KTV_song_name == cur_song_name:
            swipe([990,540],[990,332])
            if poco('com.changba.sd:id/song_item_free', timeout=1).exists():
                poco('com.changba.sd:id/songlist_item_sing', nearest=({"resourceId":'com.changba.sd:id/song_item_free'})).click()
                sleep(3)
            else:
                swipe([990,540],[990,332])
        elif  poco('正在进入演唱...', text='正在进入演唱...').exists():
            print('正在进入演唱...')
            sleep(5)
        else:
            print('unknown situation...')

if exists(Template('../../Design/KTV_playing_btn.png')) and ST.KTV_song_name:
    play_another_song()
elif ST.KTV_song_name is None:
    print("please run 'KTV_播放歌曲.tcs' before run this case")
    #do_segment(Segment('../KTV_播放歌曲.tcs'))
    error('ST.KTV_song_name is None')
if poco('录音关闭', text='录音关闭').exists():
    poco(text='录音关闭').click()