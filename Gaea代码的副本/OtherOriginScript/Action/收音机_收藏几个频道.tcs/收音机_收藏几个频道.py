from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

if poco('我的收藏', text='我的收藏', timeout=2, device=DEV1).exists():
    poco('android.widget.ImageView', pos=(0.1046875, 0.2111111111111111)).click()    

for _ in range(2):
    touch(Template('../../Design/radio_add_frenquency_button.png'), device=DEV1)
    touch_if(Template('../../Design/radio_not_favorite_icon.png'), timeout=3,device=DEV1)

touch(Template('../../Design/radio_display_button.png'), device=DEV1)
touch_if(Template('../../Design/radio_my_favorite_not_select_icon.png'), timeout=3, device=DEV1)
sleep(2)
ST.current_radio_favorite_list = snapshot(rect=[507, 144, 888, 426], device=DEV1)
touch(Template('../../Design/radio_display_return_button.png'), device=DEV1)
