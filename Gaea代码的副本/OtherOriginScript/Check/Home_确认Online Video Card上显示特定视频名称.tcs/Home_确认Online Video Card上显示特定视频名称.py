from autost.api import *

try:
    assert_exists(Template('../../Design/Home_OnlineVideo_VideoName.png'))
except:
    error('OnlineVideo Card Check!')
