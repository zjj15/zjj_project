from autost.api import *

try:
    assert_exists(Template('../../../Design/FM_Defualt_Channel.png'))
except:
    error('FM Default Channel Check Error!')