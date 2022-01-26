from autost.api import *

try:
    assert_exists(Template('../../../Design/BTInfo_init.png'))
except:
    error('BT Info init Check Error!')