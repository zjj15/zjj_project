from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

if poco('我的收藏', text='我的收藏', timeout=2, device=DEV1).exists():
    poco('android.widget.ImageView', pos=(0.1046875, 0.2111111111111111)).click()    

touch_if(Template('../../Design/radio_search_mode_icon.png'), timeout=3,device=DEV1, delay=5)
## touch之后等ons消去
#sleep(5)
try:
    assert_exists(Template('../../Design/radio_favorite_mode_icon.png'),device=DEV1)
except:
    error('set radio_favorite_mode error!') 

