from autost.api import *

try:
    assert_exists(Template("../../../Design/FaultDiag_Errorlog_Clear.png"))
except:
    error('Error List Check init Error!')