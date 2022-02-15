from autost.api import *

DEV1="Gaea://127.0.0.1:5037/GFEDCBA0987654321"

do_segment(Segment('../../Common/BackHomeView.tcs'))

flick_to(Template('../../Design/theme_shop_icon.png'), [957, 347], DIR_LEFT, step=1, speed=SPEED_NORMAL)

touch(Template('../../Design/theme_shop_icon.png'),device=DEV1)
for _ in range(4):
    if poco('允许', text='允许', timeout=1).exists():
        poco('允许', text='允许').click()
    else:
        break
touch_if(Template('../../Design/theme_shop_Notice_neverNotice.png'), timeout=5, device=DEV1)
touch_if(Template('../../Design/theme_shop_Notice_agree.png'), timeout=1, device=DEV1)
sleep(5)
# current version can not into theme shop(20210127)
try:
    assert_not_exists(Template('../../Design/theme_shop_icon.png'),device=DEV1,timeout=5) 
except:
    error('Into theme shop Error!')
