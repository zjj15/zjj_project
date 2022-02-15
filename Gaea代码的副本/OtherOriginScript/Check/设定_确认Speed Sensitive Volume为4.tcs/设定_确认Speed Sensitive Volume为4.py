from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

try:
    assert_exists(Template('../../Design/sound_setting_SpeedSensitiveVolume_4_icon.png'),device=DEV1)
except:
    error('current SpeedSensitive_Volume_step not 4 !') 
