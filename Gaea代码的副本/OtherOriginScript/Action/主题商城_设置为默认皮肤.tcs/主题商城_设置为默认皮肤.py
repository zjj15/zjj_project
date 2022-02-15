from autost.api import *
print('__脚本名称: ' + __file__)

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

touch_if(Template('../../Design/themeShop_cancel_button.png'), timeout=2, device=DEV1)
touch_if(Template('../../Design/themeShop_mine_unselected_button.png'), timeout=3, device=DEV1)

if exists(Template('../../Design/themeShop_default_theme_icon.png'), timeout=3, device=DEV1):
    touch_if(Template('../../Design/themeShop_default_theme_using.png'), timeout=3, device=DEV1)
    wait_for_appearance(Template('../../Design/themeShop_apply_success_icon.png'), device=DEV1,timeout=20)