from autost.api import *

do_segment(Segment('../../../Screen/进入Fault diagnosis.tcs'))

touch(Template('../../../Design/FaultDiag_Comfirm_Adjust.png'))

touch(Template('../../../Design/FaultDiag_AVComm.png'))

touch(Template('../../../Design/FaultDiag_AVComm_Reset.png'))

touch(Template('../../../Design/FaultDiag_Delete_Confirm.png'))

try:
    assert_exists(Template('../../../Design/FaultDiag_AVComm_Reset_Hlight.png'))
    assert_not_exists(Template('../../../Design/FaultDiag_AVComm_Select.png'))
except:
    error('AVComm Reset Error!')
