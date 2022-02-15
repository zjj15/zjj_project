from autost.api import *

do_segment(Segment('../iQIYI_选中选集list.tcs'))

flick([1752, 432], DIR_UP, step=3, speed=SPEED_NORMAL)
flick([1752, 432], DIR_UP, step=3, speed=SPEED_NORMAL)
flick([1752, 432], DIR_UP, step=3, speed=SPEED_NORMAL)

touch([1792, 435])

wait_for_appearance(Template("../../Design/OnlineVideo_Play_Bar.png"), timeout=30)
ST.OnlineVideo_variety_last = poco(className='android.widget.TextView', pos2=[307, 136]).get_attr('text')
print('时间剧集List最后一集：'+ST.OnlineVideo_variety_last)