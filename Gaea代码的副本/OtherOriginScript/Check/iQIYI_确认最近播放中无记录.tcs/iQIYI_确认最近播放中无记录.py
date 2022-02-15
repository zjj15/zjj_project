from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

video_name = get_param('videoname')

do_segment(Segment('../../Screen/进入iQIYI最近播放画面.tcs'))

recent_program_1_name = poco(className='android.widget.TextView', pos2=[238, 394]).get_attr('text')
recent_program_1_num = poco(className='android.widget.TextView', pos2=[238, 434]).get_attr('text')
recent_program_2_name = poco(className='android.widget.TextView', pos2=[468, 394]).get_attr('text')
recent_program_2_num = poco(className='android.widget.TextView', pos2=[468, 434]).get_attr('text')
recent_program_3_name = poco(className='android.widget.TextView', pos2=[698, 394]).get_attr('text')
recent_program_3_num = poco(className='android.widget.TextView', pos2=[698, 434]).get_attr('text')
prgram_C = (recent_program_1_name+recent_program_1_num).replace(" ","") if (recent_program_1_name and recent_program_1_num) else None
prgram_B = (recent_program_2_name+recent_program_2_num).replace(" ","") if (recent_program_1_name and recent_program_1_num) else None
prgram_A = (recent_program_3_name+recent_program_3_num).replace(" ","") if (recent_program_1_name and recent_program_1_num) else None
print('prgram_A:'+prgram_A)
print('prgram_B:'+prgram_B)
print('prgram_C:'+prgram_C)

cur_recent_list = [prgram_A, prgram_B, prgram_C]

if poco('暂无内容', text='暂无内容', timeout=2).exists():
    pass
else:
    print('video_name:', video_name)
    print('cur video_name:', program_1)
    if 'A' == video_name:
        print('check video_name A:', ST.OnlineVideo_program_A)
        check_text = ST.OnlineVideo_program_A.replace(" ","")
        assert check_text not in cur_recent_list
    elif 'B' == video_name:
        print('check video_name B:', ST.OnlineVideo_program_B)
        check_text = ST.OnlineVideo_program_B.replace(" ","")
        assert check_text not in cur_recent_list
    elif 'C' == video_name:
        print('check video_name C:', ST.OnlineVideo_program_C)
        check_text = ST.OnlineVideo_program_C.replace(" ","")
        assert check_text not in cur_recent_list
    else:
        error('unknown situation')