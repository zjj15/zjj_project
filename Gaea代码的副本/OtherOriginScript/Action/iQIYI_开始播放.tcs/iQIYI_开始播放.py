from autost.api import *


touch_if(Template('../../Design/OnlineVideo_Agreement_Confirm.png'), timeout=3)

touch_if(Template('../../Design/OnlineVideo_PlayScreen_return.png'), timeout=3)
touch_if(Template('../../Design/OnlineVideo_Login_cancel.png'), timeout=1)
if exists(Template('../../Design/OnlineVideo_走形规制_安全提示MSG.png'),threshold = 0.95, timeout = 2):
    do_segment(Segment('../CAN_发送PKB_ON.tcs'))
for i in range(3):
    if exists(Template('../../Design/OnlineVideo_加载失败提示.png'),threshold = 0.95, timeout = 2):
        touch([454, 437])
        sleep(5)
    elif poco('加载中…', text='加载中…', timeout=1).exists():
        sleep(5)
    else:
        break

do_segment(Segment('../iQIYI_选择tab_tabname.tcs'), tabname='电视剧')
do_segment(Segment('../iQIYI_选中免费.tcs'))
touch([862, 517])
#touch([276, 382])

try:
    wait_for_appearance(Template('../../Design/OnlineVideo_Play_Bar.png'), timeout=30)
    ST.OnlineVideo_program_start_play = poco(className='android.widget.TextView', pos2=[307, 136]).get_attr('text')
except:
    error('OnlineVideo Play Error!')
