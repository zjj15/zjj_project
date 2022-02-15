from autost.api import *

touch(Template('../../Design/FaultDiag_Comfirm_Adjust.png'))

touch(Template('../../Design/FaultDiag_Error_Log.png'))
try:
    assert_exists(Template('../../Design/FaultDiag_Delete_Errorlog.png'))
except:
    error('Into Error List Error!')
