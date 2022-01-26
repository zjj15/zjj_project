from autost.api import *

if exists(Template('../../Design/OnlineVideo_筛选中.png'), timeout=2):
    touch(Template('../../Design/OnlineVideo_筛选中.png'), timeout=2)
touch(Template('../../Design/OnlineVideo_筛选.png'), timeout=2)
for i in range(5):
    if exists(Template('../../Design/OnlineVideo_筛选_自制_选中.png'), timeout=1):
        break
    elif exists(Template('../../Design/OnlineVideo_筛选_自制.png'), timeout=1):
        touch(Template('../../Design/OnlineVideo_筛选_自制.png'), timeout=5)
    else:
        flick([519, 521], DIR_RIGHT, step=2, speed=SPEED_FAST)
assert_exists(Template('../../Design/OnlineVideo_筛选_自制_选中.png'), timeout=2)
sleep(3)
