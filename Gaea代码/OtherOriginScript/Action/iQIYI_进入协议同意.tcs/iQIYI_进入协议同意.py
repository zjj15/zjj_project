from autost.api import *

try:
    touch_if(Template('../../Design/OnlineVideo_Agreement_Confirm.png'), timeout=10)
    #assert_exists(Template('../../Design/OnlineVideo_Center.png'))
except:
    error('OnlineVdieo Confirm Error!')
