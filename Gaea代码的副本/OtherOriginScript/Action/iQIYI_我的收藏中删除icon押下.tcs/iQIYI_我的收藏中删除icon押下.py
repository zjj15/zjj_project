from autost.api import *
#
DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

do_segment(Segment('../../Screen/进入iQIYI我的收藏画面.tcs'))

touch_if(Template('../../Design/OnlineVideo_favourite_delete_icon.png'), timeout=3,device=DEV1)
