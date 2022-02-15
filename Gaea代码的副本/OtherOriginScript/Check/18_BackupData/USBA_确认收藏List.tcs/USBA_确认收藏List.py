from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

touch(Template('../../../Design/usbaudio_display_button.png'), device=DEV1)
touch_if(Template('../../../Design/usbaudio_my_favorite_next_selected_icon.png'), timeout=3, device=DEV1)
sleep(2)
try:
    assert_exists(ST.usbaudio_favorite_list,device=DEV1)
except:
    error('check usbaudio favorite list fail!') 
touch(Template('../../../Design/usbaudio_display_return_button.png'), device=DEV1)
