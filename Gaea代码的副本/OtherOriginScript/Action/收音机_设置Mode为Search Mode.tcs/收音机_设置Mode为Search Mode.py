from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

## fix：ons弹出，touch 失败
for _ in range(3):
    touch_if(Template('../../Design/radio_favorite_mode_icon.png'), timeout=1,device=DEV1)
    if exists(Template('../../Design/radio_search_mode_icon.png'), timeout=2, device=DEV1):
        break

try:
    assert_exists(Template('../../Design/radio_search_mode_icon.png'),device=DEV1)
except:
    error('Into radio_search_mode error!') 

