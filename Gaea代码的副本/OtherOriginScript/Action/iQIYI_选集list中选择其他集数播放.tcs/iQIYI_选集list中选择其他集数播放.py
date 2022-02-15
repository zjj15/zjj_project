from autost.api import *

do_segment(Segment('../iQIYI_选中选集list.tcs'))

program_cur = poco(className='android.widget.TextView', pos2=[307, 136]).get_attr('text')
program_cur_st = poco(className='android.widget.TextView',org_size=(62, 34), selected=True).get_attr('text')
print('当前播放视频：'+program_cur)
print('当前播放视频集数：'+program_cur_st)

poco(className='android.widget.TextView',org_size=(62, 34), selected=False).click()
wait_for_appearance(Template("../../Design/OnlineVideo_Play_Bar.png"), timeout=300)

program_other = poco(className='android.widget.TextView', pos2=[307, 136]).get_attr('text')
print('选择其他的视频：'+program_other)
if program_cur==program_other:
    error('iQIYI_选集list中选择其他集数播放 error!!!')
