from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print('__脚本名称: ' + __file__)



if exists(Template('../../../Design/Statusbar_Navi_1.png'), timeout=1, threshold=0.90):
    pass
elif exists(Template('../../../Design/Statusbar_Navi_2.png'), timeout=1, threshold=0.90):
    pass
else:
    do_segment(Segment('../../../Common/BackHomeView.tcs'))
    poco('GPS定位中…', text='GPS定位中…').click()
    sleep(2)

for i in range(3):
    touch_if(Template('../../../Design/Navi_允许.png'), timeout=1, device=DEV1)

touch_if(Template('../../../Design/GaodeNavi_Notice_neverNotice.png'), timeout=3, device=DEV1)
touch_if(Template('../../../Design/GaodeNavi_Notice_agree.png'), timeout=3, device=DEV1)
touch_if(Template("../../../Design/Navi_左侧弹出框.png"), timeout=1.5, threshold=0.90, device=DEV1)
touch_if(Template('../../../Design/Navi_close.png'), timeout=3, device=DEV1)
touch_if(Template("../../../Design/Navi_左侧弹出框.png"), timeout=1.5, threshold=0.90, device=DEV1)
touch_if(Template('../../../Design/Navi_menu_back.png'), threshold=0.93, timeout=1, device=DEV1)
touch_if(Template('../../../Design/Navi_menu_back.png'), threshold=0.93, timeout=1, device=DEV1)

assert_exists(Template('../../../Design/Navi_target.png'), device=DEV1)
