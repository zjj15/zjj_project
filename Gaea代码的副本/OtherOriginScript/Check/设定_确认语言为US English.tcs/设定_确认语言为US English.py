from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

flick([1000, 300], DIR_DOWN, step=3, speed=SPEED_NORMAL,device=DEV1)
flick([1000, 300], DIR_DOWN, step=3, speed=SPEED_NORMAL,device=DEV1)

try:
    assert_exists(Template('../../Design/language_English_selected_icon.png'),device=DEV1)
except:
    error('set language_English error!') 

