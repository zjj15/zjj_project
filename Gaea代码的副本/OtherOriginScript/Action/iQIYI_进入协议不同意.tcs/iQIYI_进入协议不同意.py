from autost.api import *

try:
    touch(Template('../../Design/OnlineVideo_Argeement_disagree.png'))
    assert_not_exists(Template('../../Design/OnlineVideo_Center.png'), timeout=5)
except:
    error('OnlineVideo Argeement disagree Error!')
