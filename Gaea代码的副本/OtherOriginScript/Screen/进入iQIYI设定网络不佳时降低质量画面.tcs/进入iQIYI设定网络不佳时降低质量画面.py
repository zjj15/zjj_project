from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

do_segment(Segment('../../Action/iQIYI_播放免费视频.tcs'))

# enter bitstream quality setting screen
touch([318, 646],device=DEV1)

try:
    assert_exists(Template('../../Design/OnlineVideo_BitStreamQualit_icon.png'),device=DEV1,timeout =5)
except:
    error('enter onlinevideo bitstream quality setting screen Fail!')