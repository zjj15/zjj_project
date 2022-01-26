from autost.api import *

touch_if(Template('../../Design/OnlineVideo_PlayScreen_return.png'), timeout=3)
do_segment(Segment('../iQIYI_取消Filter.tcs'))

do_segment(Segment('../iQIYI_选择tab_tabname.tcs'), tabname='电视剧')
do_segment(Segment('../iQIYI_选中免费.tcs'))
touch([862, 517])

try:
    wait_for_appearance(Template('../../Design/OnlineVideo_Play_Bar.png'), timeout=30)
    ST.OnlineVideo_program_B = poco(className='android.widget.TextView', pos2=[307, 136]).get_attr('text')
    print('iQIYI_播放任意视频_B:'+ST.OnlineVideo_program_B)
except:
    error('iQIYI_播放免费视频 Play Error!')
