from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

print("__脚本名称: " + __file__)

assert_exists(Template('../../Design/Music_USBAudio_btn_focus.png'), device=DEV1)
try:
    assert_exists(Template('../../Design/USBAudio_PlayBar.png'))
except:
    error('USB Audio Play Error!s')
