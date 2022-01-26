from autost.api import *

do_segment(Segment('../iQIYI_搜索VIP视频.tcs'))

if exists(Template('../../Design/OnlineVideo_加载失败提示.png'),threshold =0.9):
    touch([956, 430])
if exists(Template('../../Design/OnlineVideo_vip_icon.png'), timeout=1,threshold = 0.88):
    touch(Template('../../Design/OnlineVideo_vip_icon.png'), timeout=1,threshold = 0.88)
elif exists(Template('../../Design/OnlineVideo_vip_icon_big.png'), timeout=1,threshold = 0.88):
    touch(Template('../../Design/OnlineVideo_vip_icon_big.png'), timeout=1,threshold = 0.88)
else:
    touch([868, 339])
 
wait_for_appearance(Template('../../Design/OnlineVideo_Play_Bar.png'), timeout=30)
for i in range(3):
    if exists(Template('../../Design/OnlineVideo_vip_icon.png'), timeout=1,threshold = 0.88):
        touch(Template('../../Design/OnlineVideo_vip_icon.png'), timeout=1, threshold = 0.88)
        break
    else:
        flick([1756, 449], DIR_UP, step=2, speed=SPEED_NORMAL)

#wait_for_appearance(Template('../../Design/OnlineVideo_VIP视频试看6分钟提示.png'), timeout=20,threshold = 0.88)
