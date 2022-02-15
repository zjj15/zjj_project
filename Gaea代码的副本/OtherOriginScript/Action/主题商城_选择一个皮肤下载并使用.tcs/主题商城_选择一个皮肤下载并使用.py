from autost.api import *
print('__脚本名称: ' + __file__)

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

touch_if(Template('../../Design/themeShop_cancel_button.png'), timeout=2, device=DEV1)
touch_if(Template('../../Design/themeShop_shop_unselected_button.png'), timeout=3, device=DEV1)


touch(Template('../../Design/themeShop_scinece_theme_icon.png'), timeout=3, device=DEV1, threshold=0.8)
if not exists(Template('../../Design/themeShop_theme_using.png'), device=DEV1,timeout=3):
    touch_if(Template('../../Design/themeShop_theme_downAndUse.png'), device=DEV1,timeout=2)
    touch_if(Template('../../Design/themeShop_scinece_theme_use_icon.png'), device=DEV1,timeout=2)
    if poco('去登录', text='去登录', timeout=2).exists():
        poco(text='去登录').click()
        do_segment(Segment('../设定时间同步.tcs'))
        sleep(3)
        touch_if(Template('../../Design/themeShop_cancel_button.png'), timeout=2, device=DEV1)

        #do_segment(Segment('../个人中心登录_账号1.tcs'))
 
    if exists(Template('../../Design/themeShop_theme_using.png'), device=DEV1,timeout=3):
        pass
    else:
        touch_if(Template('../../Design/themeShop_theme_downLoad.png'), device=DEV1,timeout=2)
 
        wait_for_appearance(Template('../../Design/themeShop_apply_success_icon.png'), device=DEV1,timeout=20)

assert_exists(Template('../../Design/themeShop_theme_using.png'), device=DEV1,timeout=3)
touch_if(Template('../../Design/themeShop_cancel_button.png'), timeout=2, device=DEV1)