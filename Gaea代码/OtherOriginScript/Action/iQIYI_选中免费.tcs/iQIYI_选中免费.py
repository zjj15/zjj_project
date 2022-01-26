from autost.api import *

do_segment(Segment('../iQIYI_取消Filter.tcs'))
touch(Template('../../Design/OnlineVideo_筛选.png'), timeout=2)

for i in range(5):
    flick([598, 389], DIR_LEFT, step=2, speed=SPEED_FAST)
    if exists(Template('../../Design/OnlineVideo_筛选_免费_选中.png'), timeout=1):
        break
    elif exists(Template('../../Design/OnlineVideo_筛选_免费.png'), timeout=1):
        touch(Template('../../Design/OnlineVideo_筛选_免费.png'), timeout=5)
assert_exists(Template('../../Design/OnlineVideo_筛选_免费_选中.png'), timeout=1)
sleep(3)
