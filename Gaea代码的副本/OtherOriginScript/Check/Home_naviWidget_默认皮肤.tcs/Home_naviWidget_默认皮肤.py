from autost.api import *

try:
    assert_exists(Template('../../Design/Home_NaviWidget_defaultSkin.png'),timeout=5)
except:
    error('not NaviWidget default skin')
