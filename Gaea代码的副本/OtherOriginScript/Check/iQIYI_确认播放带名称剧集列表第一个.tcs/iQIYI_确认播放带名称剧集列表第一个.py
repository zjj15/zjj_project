from autost.api import *
#iQIYI_播放任意有名称的剧集列表:少儿频道免费视频
program_cur = poco(className='android.widget.TextView', pos2=[307, 136]).get_attr('text')
print('当前播放视频：'+program_cur)
for i in range(20):
    program = poco(className='android.widget.TextView', pos2=[307, 136]).get_attr('text')
    if program_cur == program:
        sleep(3)
    else:
        break

sleep(5)
assert_exists(Template('../../Design/OnlineVideo_Play_Bar.png'), timeout=30)

cur_program = poco(className='android.widget.TextView', pos2=[307, 136]).get_attr('text')
print('【确认带名称剧集】当前播放内容：'+cur_program)
print('【确认带名称剧集】期待播放内容：'+ST.OnlineVideo_Children_1st)
if ST.OnlineVideo_Children_1st == cur_program:
    pass
else:
    error('iQIYI_确认播放带名称剧集列表第一个 error!!!')
