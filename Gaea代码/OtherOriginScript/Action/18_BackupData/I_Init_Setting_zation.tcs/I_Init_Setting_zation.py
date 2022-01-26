from autost.api import *

do_segment(Segment('../../../Screen/进入Fault diagnosis.tcs'))

touch(Template('../../../Design/FaultDiag_Comfirm_Adjust.png'))

flick_to(Template('../../../Design/FaultDiag_Initalization.png'), [1180, 400], DIR_UP, step=1, speed=SPEED_NORMAL)

sleep(1)

touch(Template('../../../Design/FaultDiag_Initalization.png'))

touch(Template('../../../Design/FaultDiag_Delete_Confirm.png'))

#sleep(2)

try:
    assert_exists(Template('../../../Design/FaultDiag_Initlalization_wait.png'),timeout=22)
except:
    error('Ininialize Settings Initialization Error!')
