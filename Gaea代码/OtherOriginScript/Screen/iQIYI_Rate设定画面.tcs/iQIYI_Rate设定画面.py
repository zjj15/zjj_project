from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
if exists(Template('../../Design/OnlineVideo_Play_Bar.png'), threshold=0.95,timeout =1):
    touch([567, 633],device=DEV1)
elif exists(Template('../../Design/OnlineVideo_Rate_icon.png'),device=DEV1,timeout =1):
    pass
else:
    do_segment(Segment('../../Action/iQIYI_播放免费视频.tcs'))
    # enter rateSetting screen
    touch([567, 633],device=DEV1)
try:
    assert_exists(Template('../../Design/OnlineVideo_Rate_icon.png'),device=DEV1,timeout =5)
except:
    error('enter onlinevideo rate setting screen Fail!')
 