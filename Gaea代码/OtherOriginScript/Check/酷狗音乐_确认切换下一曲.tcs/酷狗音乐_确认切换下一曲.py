from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print('__脚本名称: ' + __file__)

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

cur_song_name = poco(className='android.widget.TextView', pos2=[1540, 177] ).get_attr('text')
print('cur_song_name：', cur_song_name)

try:
    if cur_song_name == ST.OnlineMusic_song_next:
        print('expect song name：', ST.OnlineMusic_song_next)
        error('__脚本名称: ' + __file__+ 'Check error')
    else:
        print('kugou is playing')
finally:
    pass#ST.OnlineMusic_song_name = None
