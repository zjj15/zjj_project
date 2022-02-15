from autost.api import *

DEV1 = ST.DEV1

touch(Template('../../Design/usbaudio_display_button.png'), device=DEV1)
touch_if(Template('../../Design/usbaudio_my_favorite_next_selected_icon.png'), timeout=3, device=DEV1)
sleep(2)
try:
    assert_exists(Template('../../Design/check_usbaudio_favorite_list_null.png'),device=DEV1)

except:
    error('check usbaudio favorite list null fail!') 
touch(Template('../../Design/usbaudio_display_return_button.png'), device=DEV1)
