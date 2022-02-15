from autost.api import *

try:
    assert_exists(Template('../../Design/OnlineVideo_Agreement_Check.png'))
    assert_exists(Template('../../Design/OnlineVideo_Agreement_Confirm.png'))
    assert_exists(Template('../../Design/OnlineVideo_Argeement_disagree.png'))
except:
    error('OnlineVideo Agreement Check Error!')
 
 
