from autost.api import *
print('__脚本名称: ' + __file__)

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
for i in range(3):
    touch_if(Template('../../Design/radio_pause_btn.png'), timeout=1, device=DEV1)

try:
    assert_exists(Template('../../Design/radio_playing_btn.png'),device=DEV1)

except:
    error(__file__+' error!') 


