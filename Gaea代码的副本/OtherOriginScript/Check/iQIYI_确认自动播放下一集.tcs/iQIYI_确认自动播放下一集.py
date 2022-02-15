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

program_next_st = poco(className='android.widget.TextView',org_size=(62, 34), selected=True).get_attr('text')
program_next = poco(className='android.widget.TextView', pos2=[307, 136]).get_attr('text')
print('下一集播放：'+program_next)
print('当前播放视频集数：'+program_next_st)
if int(program_next_st) != int(program_cur_st)+1:
    error('iQIYI_确认自动播放下一集 error!!!')

 
