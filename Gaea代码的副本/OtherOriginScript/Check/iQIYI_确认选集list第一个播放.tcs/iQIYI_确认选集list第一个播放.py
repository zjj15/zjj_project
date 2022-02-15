from autost.api import *

assert_exists(Template('../../Design/OnlineVideo_Play_Bar.png'), timeout=30)
poco(text='选集').click()

flick([1783, 224], DIR_DOWN, step=3, speed=SPEED_NORMAL)
flick([1783, 224], DIR_DOWN, step=3, speed=SPEED_NORMAL)
flick([1783, 224], DIR_DOWN, step=3, speed=SPEED_NORMAL)

sleep(5)
cur_program = poco(className='android.widget.TextView', pos2=[307, 136]).get_attr('text')
print('当前播放视频：'+cur_program)
if cur_program == ST.OnlineVideo_any_last:
    error('iQIYI_确认选集list第一个播放 error!!!')
