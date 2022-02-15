from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print('__脚本名称: ' + __file__)

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

cur_song_info_1 = poco(className='android.widget.TextView', pos2=[828, 625] ).get_attr('text')
print('cur_song_name:', cur_song_info_1)

try:
    if ST.OnlineRadio_program_previous == cur_song_info_1:
        print('kugou is playing')
    else:
        print('expect song name：', ST.OnlineRadio_program_previous)
        error('__脚本名称: ' + __file__+ 'Check error')
finally:
    pass
