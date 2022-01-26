from autost.api import *

if exists(Template('../../Design/OnlineVideo_Play_Bar.png'), threshold=0.95,timeout =1):
    pass
else:
    do_segment(Segment('../../Action/iQIYI_播放免费视频.tcs'))
try:
    assert_exists(Template('../../Design/OnlineVideo_PlayScreen_Rate_1.25.png'))
except:
    error('OnlinVideo Rate_1.25 Check Error!')
