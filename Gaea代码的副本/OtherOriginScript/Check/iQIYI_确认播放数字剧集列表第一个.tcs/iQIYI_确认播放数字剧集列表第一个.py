from autost.api import *

program_cur = poco(className='android.widget.TextView', pos2=[307, 136]).get_attr('text')
program_cur_st = poco(className='android.widget.TextView',org_size=(62, 34), selected=True).get_attr('text')
print('当前播放视频：'+program_cur)
print('当前播放视频集数：'+program_cur_st)
for i in range(20):
    program = poco(className='android.widget.TextView', pos2=[307, 136]).get_attr('text')
    if program_cur == program:
        sleep(10)
    else:
        break
sleep(5)

assert_exists(Template('../../Design/OnlineVideo_Play_Bar.png'), timeout=30)

cur_program = poco(className='android.widget.TextView', pos2=[307, 136]).get_attr('text')
print('数字剧集当前播放：'+cur_program)
if ST.OnlineVideo_Num_1st != cur_program:
    print('【确认数字剧集列】期待播放内容：'+ST.OnlineVideo_Num_1st)