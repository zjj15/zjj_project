from autost.api import *

if exists(Template('../../Design/OnlineVideo_推荐_focus.png'), timeout=2) or exists(Template('../../Design/OnlineVideo_推荐_nofocus.png'), timeout=2):
    touch_if(Template('../../Design/OnlineVideo_推荐_nofocus.png'), timeout=1)
    wait_for_disappearance(Template('../../Design/OnlineVideo_推荐list_空.png'), timeout=30)
else:
    error('iQIYI_确认播放中视频有推荐栏 error!!!')
