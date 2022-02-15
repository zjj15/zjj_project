from autost.api import *


do_segment(Segment("../iQIYI_选中选集list.tcs"))

flick([1846, 223], DIR_LEFT, step=3, speed=SPEED_NORMAL)
touch([1837, 223])
wait_for_disappearance(Template("../../Design/OnlineVideo_选集list_空.png"), timeout=30)

flick([1752, 432], DIR_UP, step=3, speed=SPEED_NORMAL)
flick([1752, 432], DIR_UP, step=3, speed=SPEED_NORMAL)
flick([1752, 432], DIR_UP, step=3, speed=SPEED_NORMAL)

touch([1792, 435])

wait_for_appearance(Template("../../Design/OnlineVideo_Play_Bar.png"), timeout=30)
ST.OnlineVideo_Children_last = poco(className='android.widget.TextView', pos2=[307, 136]).get_attr('text')
print('带名称剧集List最后一集：'+ST.OnlineVideo_Children_last)
