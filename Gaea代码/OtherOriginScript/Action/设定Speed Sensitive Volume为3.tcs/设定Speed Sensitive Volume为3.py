from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

touch(ST.SpeedSensitive_Volume_step3_Point, device=DEV1)
try:
    assert_exists(Template('../../Design/sound_setting_SpeedSensitiveVolume_3_icon.png'),device=DEV1)
except:
    error('set SpeedSensitive_Volume_step3 fail!') 
