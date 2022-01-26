from autost.api import *

do_segment(Segment('../../../Screen/进入Fault diagnosis.tcs'))

touch(Template('../../../Design/FaultDiag_Comfirm_Adjust.png'))

touch(Template('../../../Design/FaultDiag_Error_Log.png'))

touch(Template('../../../Design/FaultDiag_Delete_Errorlog.png'))

touch(Template('../../../Design/FaultDiag_Delete_Confirm.png'))

try:
    assert_exists(Template('../../../Design/FaultDiag_Errorlog_Clear.png'))
except:
    error('The LOG of error list reset Error!')

