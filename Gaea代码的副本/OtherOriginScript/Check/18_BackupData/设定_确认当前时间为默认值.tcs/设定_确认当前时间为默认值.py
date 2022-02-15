from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

# set time setting off
if exists(Template('../../../Design/24hour_setting_off_icon.png'), timeout=3,device=DEV1):
    touch_in(Template('../../../Design/setting_off_icon.png'),Template('../../../Design/24hour_setting_off_icon.png'), device=DEV1)

if exists(Template('../../../Design/time_Autoset_setting_on_icon.png'), timeout=3,device=DEV1):
    touch_in(Template('../../../Design/setting_on_icon.png'),Template('../../../Design/time_Autoset_setting_on_icon.png'), device=DEV1)


# confirm time default
try:
    #assert_exists(Template('../../../Design/default_time.png'),device=DEV1)
    assert_exists(Template('../../../Design/default_time_3.png'),device=DEV1)
    assert_exists(Template('../../../Design/default_time_2.png'),device=DEV1)
except:
    error('check current time  0:00 error!') 
