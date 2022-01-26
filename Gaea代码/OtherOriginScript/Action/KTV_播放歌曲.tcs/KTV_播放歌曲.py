from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print("__脚本名称: " + __file__)

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
do_segment(Segment('../DrivingRestrictOff.tcs'))

for i in range(10):
    if exists(Template('../../Design/KTV_playing_btn.png'), threshold=0.9):
        break
    if poco(text='录音保存中，马上就好').exists():
        sleep(3)
    elif poco('正在加载,请稍候', text='正在加载,请稍候', timeout=1).exists():
        sleep(10)
    elif poco('com.changba.sd:id/song_item_free', timeout=1).exists():
        poco('com.changba.sd:id/songlist_item_sing', nearest=({"resourceId":'com.changba.sd:id/song_item_free'})).click()
        sleep(1)
        if poco(text='麦克风未连接', timeout =3).exists():
            poco(text='忽略').click()
        sleep(1)
    elif poco('录音关闭', text='录音关闭').exists():
        poco(text='录音关闭').click()
    else:
        swipe([990,540],[990,332])
else:
    error(__file__+'error')

cur_song_name = poco(resourceId='com.changba.sd:id/playing_songinfo_tiny_song').get_attr('text')
ST.KTV_song_name = cur_song_name
