from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

do_segment(Segment("../../Screen/进入iQIYI我的收藏画面.tcs"))

video_name = get_param('videoname')
program_1=None

recent_program_1_name = poco(className='android.widget.TextView', pos2=[238, 394], timeout=2).get_attr('text')
recent_program_1_num = poco(className='android.widget.TextView', pos2=[238, 434], timeout=2).get_attr('text')
if recent_program_1_name:
    program_1= recent_program_1_name.replace(" ","")

print('cur video_name:', program_1)
if poco('暂无收藏内容', text='暂无收藏内容', timeout=2).exists():
    pass
else:
    if 'A' == video_name:
        print('expect video_name A:', ST.OnlineVideo_program_A)
        idx = ST.OnlineVideo_program_A.index('第')
        check_text = ST.OnlineVideo_program_A[:idx]
        assert check_text.replace(" ","") != program_1
    elif 'B' == video_name:
        print('expect video_name B:', ST.OnlineVideo_program_B)
        idx = ST.OnlineVideo_program_B.index('第')
        check_text = ST.OnlineVideo_program_B[:idx]
        assert check_text.replace(" ","") != program_1
    elif 'C' == video_name:
        print('expect video_name C:', ST.OnlineVideo_program_C)
        idx = ST.OnlineVideo_program_C.index('第')
        check_text = ST.OnlineVideo_program_C[:idx]
        assert check_text.replace(" ","") != program_1
    else:
        error('unknown situation')