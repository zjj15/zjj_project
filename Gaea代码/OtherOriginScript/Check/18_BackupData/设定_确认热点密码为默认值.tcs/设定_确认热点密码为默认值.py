from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

if exists(Template('../../../Design/hot_point_off_icon.png'), timeout=3,device=DEV1):
    touch_in(Template('../../../Design/setting_off_icon.png'),Template('../../../Design/hot_point_off_icon.png'), device=DEV1)


try:
    assert_not_exists(Template('../../../Design/hotpoint_changed_password_icon.png'),device=DEV1)
except:
    error('check default hotpoint password fail!') 
