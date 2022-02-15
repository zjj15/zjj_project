from autost.api import *

DEV1 = ST.DEV1
touch(Template('../../Design/radio_display_button.png'), device=DEV1)
touch_if(Template('../../Design/radio_my_favorite_not_select_icon.png'), timeout=3, device=DEV1)
sleep(2)
try:
    assert_exists(Template('../../Design/check_radio_favorite_list_default.png'),device=DEV1)
 
except:
    error('check radio favorite_list default error!') 
touch(Template('../../Design/radio_display_return_button.png'), device=DEV1)
