from autost.api import *

try:
    assert_exists(Template('../../Design/Home_NaviWidget_Amap_defaultSkin.png'),timeout=5,threshold=0.7)
except:
    error('not NaviWidget default skin with Amap app')
