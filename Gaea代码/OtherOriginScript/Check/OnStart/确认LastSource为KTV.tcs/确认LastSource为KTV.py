from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
#重启后会显示游客登录
sleep(15)
print('__脚本名称: ' + __file__)

if (not exists(Template("../../../Design/Home_mark_focus.png"), timeout=2,threshold=0.90, device=DEV1) and not exists(Template("../../../Design/Home_mark_nofocus.png"), timeout=2,threshold=0.90, device=DEV1)):
    wait_for_appearance(Template("../../../Design/Home_Page1_Bar.png"), timeout=60, device=DEV1)

do_segment(Segment("../../../Common/BackHomeView.tcs"))
try:
    assert_exists(Template('../../../Design/statusbar_ktv_unselected.png'), threshold=0.90, device=DEV1)
except:
    error('__脚本名称: ' + __file__+ 'Check error')
