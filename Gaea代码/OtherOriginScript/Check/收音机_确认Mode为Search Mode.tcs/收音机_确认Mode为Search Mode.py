from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

try:
    assert_exists(Template('../../Design/radio_search_mode_icon.png'),device=DEV1)
except:
    error('Into radio_search_mode error!') 

