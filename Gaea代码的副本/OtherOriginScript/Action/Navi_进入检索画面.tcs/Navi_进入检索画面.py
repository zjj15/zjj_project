from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

while exists(Template('../../Design/Navi_menu_back.png'), timeout=3, threshold=0.93, device=DEV1):
    touch_if(Template('../../Design/Navi_menu_back.png'), timeout=3, threshold=0.93, device=DEV1)

touch(Template('../../Design/Navi_target.png'), threshold=0.90, device=DEV1)

touch(Template('../../Design/Navi_searchBar.png'), timeout=1.5, threshold=0.93)
try:
    assert_exists(Template('../../Design/Navi_search_input_num_icon.png'), timeout=1.5, threshold=0.93)
except:
    error('Navi enter search screen Error!')
