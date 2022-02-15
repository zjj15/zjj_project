from autost.api import *

touch_if(Template('../../Design/OnlineVideo_PlayScreen_return.png'), timeout=3)
do_segment(Segment("../iQIYI_取消Filter.tcs"))

do_segment(Segment('../iQIYI_选择tab_tabname.tcs'), tabname='电视剧')
do_segment(Segment('../iQIYI_选中免费.tcs'))
touch([862, 517])

try:
    assert_exists(Template('../../Design/OnlineVideo_Play_Bar.png'), timeout=30)
    ST.OnlineVideo_program_B = poco(className='android.widget.TextView', pos2=[307, 136]).get_attr('text')
    sleep(600)
except:
    error('iQIYI_播放免费视频 Play Error!')
