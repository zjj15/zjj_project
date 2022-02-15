from autost.api import *

try:
    assert_exists(Template('../../../Design/USBAudio_Playtime_00.01.png'))
except:
    error('USB Audio Play time init Check Error!')