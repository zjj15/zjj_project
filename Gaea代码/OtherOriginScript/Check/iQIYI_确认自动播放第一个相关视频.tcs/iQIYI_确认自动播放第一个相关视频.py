from autost.api import *
program_cur = poco(className='android.widget.TextView', pos2=[307, 136]).get_attr('text')
print('当前播放视频：'+program_cur)
for i in range(20):
    program = poco(className='android.widget.TextView', pos2=[307, 136]).get_attr('text')
    if program_cur == program:
        sleep(10)
    else:
        break
sleep(5)
assert_exists(Template('../../Design/OnlineVideo_Play_Bar.png'), timeout=30)

cur_program = poco(className='android.widget.TextView', pos2=[307, 136]).get_attr('text')
if cur_program != ST.OnlineVideo_relevant:
    error('iQIYI_确认自动播放第一个相关视频 error!!!')