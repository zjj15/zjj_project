from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print('__脚本名称: ' + __file__)

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

cur_song_info_1 = poco(className='android.widget.TextView', pos2=[994, 362] ).get_attr('text')
print('cur_song_Artist:', cur_song_info_1)
cur_song_info_2 = poco(className='android.widget.TextView', pos2=[994, 406] ).get_attr('text')
print('cur_song_name_2:', cur_song_info_2)

try:
    if ST.OnlineRadio_program_previous == cur_song_info_1 or ST.OnlineRadio_program_previous == cur_song_info_2:
        print('kugou is playing')
    elif ST.OnlineRadio_program_previous:
        expect_program = ST.OnlineRadio_program_previous
        expect_program_split_list = ST.OnlineRadio_program_previous.split(' ')
        if len(expect_program_split_list)>1:
            expect_program=(expect_program_split_list[-1]).replace(" ","")
        else:
            pass
        if expect_program == cur_song_info_1.replace(" ","") or expect_program == cur_song_info_2.replace(" ",""):
            print('kugou is playing')
        else:
            print('expect song name：', ST.OnlineRadio_program_previous)
            error(__file__+ ' expect song name：' + ST.OnlineRadio_program_previous)
    else:
        print('expect song name：', ST.OnlineRadio_program_previous)
        error(__file__+ ' expect song name：' + ST.OnlineRadio_program_previous)
finally:
    pass