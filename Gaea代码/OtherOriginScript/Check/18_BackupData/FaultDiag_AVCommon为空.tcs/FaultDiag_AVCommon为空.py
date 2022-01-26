from autost.api import *

try:
    assert_exists(Template('../../../Design/AVCommon_Clear.png'))
except:
    error('AVCommon Check init Error!')