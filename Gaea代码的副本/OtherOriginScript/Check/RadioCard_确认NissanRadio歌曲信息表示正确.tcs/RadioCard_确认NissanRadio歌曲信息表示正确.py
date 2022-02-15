from autost.api import *
print("__脚本名称: " + __file__)

do_segment(Segment('../../Common/BackHomeView.tcs'))

try:
    rect_target_area=poco('android.widget.ImageView', nearest=({'text':'电台'})).get_attr('rect')
    x, y, w, h = rect_target_area
    print(rect_target_area)
    cur_song_info_1 = poco(className='android.widget.TextView', pos2=[994, 362] ).get_attr('text')
    cur_song_info_2 = poco(className='android.widget.TextView', pos2=[994, 406] ).get_attr('text')
    print('cur_song_name：%s, %s'%(cur_song_info_1, cur_song_info_2))
    if ST.OnlineRadio_program_name == cur_song_info_1 or ST.OnlineRadio_program_name == cur_song_info_2:
        print('PASSED! cur_song_name：%s, %s'%(cur_song_info_1, cur_song_info_2))
    elif ST.OnlineRadio_program_name:
        expect_program = ST.OnlineRadio_program_name
        expect_program_split_list = ST.OnlineRadio_program_name.split(' ')
        if len(expect_program_split_list)>1:
            expect_program=(expect_program_split_list[-1]).replace(" ","")
        else:
            pass
        if expect_program == cur_song_info_1.replace(" ","") or expect_program == cur_song_info_2.replace(" ",""):
            print('PASSED! kugou is playing')
        else:
            print('expect song name：', ST.OnlineRadio_program_name)
            error(__file__+ ' expect song name：' + ST.OnlineRadio_program_name)
    else:
        print('expect song name:%s'%ST.OnlineRadio_program_name)
        error(__file__+ ' expect song name：' + ST.OnlineRadio_program_name)
except:
    error(__file__+' Error!')