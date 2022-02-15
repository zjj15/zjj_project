from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

touch(Template('../../../Design/radio_display_button.png'), device=DEV1)
touch_if(Template('../../../Design/radio_my_favorite_not_select_icon.png'), timeout=3, device=DEV1)
sleep(2)
try:
    assert_exists(ST.current_radio_favorite_list,device=DEV1)
except:
    error('check radio favorite_list error!') 
touch(Template('../../../Design/radio_display_return_button.png'), device=DEV1)
