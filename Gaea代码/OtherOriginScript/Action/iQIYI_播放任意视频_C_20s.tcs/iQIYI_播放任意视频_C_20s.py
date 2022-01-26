from autost.api import *

touch_if(Template('../../Design/OnlineVideo_PlayScreen_return.png'), timeout=1)

if exists(Template('../../Design/OnlineVideo_走形规制_安全提示MSG.png'),threshold = 0.95, timeout = 2):
    do_segment(Segment('../CAN_发送PKB_ON.tcs'))

do_segment(Segment('../iQIYI_选择tab_tabname.tcs'), tabname='电视剧')
do_segment(Segment('../iQIYI_选中免费.tcs'))
touch([1079, 352])

try:
    assert_exists(Template('../../Design/OnlineVideo_Play_Bar.png'), timeout=30)
    ST.OnlineVideo_program_C = poco(className='android.widget.TextView', pos2=[307, 136]).get_attr('text')
    sleep(20)
except:
    error('iQIYI_播放免费视频 Play Error!')
