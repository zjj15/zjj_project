from autost.api import *
#任意时间剧集列表：免费综艺
print('任意时间剧集列表：免费综艺')
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
print('时间剧集当前播放：'+cur_program)
if ST.OnlineVideo_variety_1st != cur_program:
    print('【确认时间剧集】期待播放内容：'+ST.OnlineVideo_variety_1st)