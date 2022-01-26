from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print("__脚本名称: " + __file__)
for i in range(3):
    touch_if(Template('../../Design/Navi_允许.png'), timeout=1, device=DEV1)

touch_if(Template('../../Design/GaodeNavi_Notice_neverNotice.png'), timeout=3, device=DEV1)
touch_if(Template('../../Design/GaodeNavi_Notice_agree.png'), timeout=3, device=DEV1)
touch_if(Template('../../Design/Navi_close.png'), timeout=3, device=DEV1)
touch_if(Template('../../Design/Navi_menu_back.png'), threshold=0.93, timeout=1, device=DEV1)
touch_if(Template('../../Design/Navi_menu_back.png'), threshold=0.93, timeout=1, device=DEV1)
assert_exists(Template('../../Design/Navi_target.png'), device=DEV1)
