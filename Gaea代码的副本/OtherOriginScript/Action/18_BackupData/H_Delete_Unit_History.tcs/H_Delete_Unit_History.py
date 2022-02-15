from autost.api import *

do_segment(Segment("../../../Screen/进入Fault diagnosis.tcs"))

touch(Template('../../../Design/FaultDiag_Comfirm_Adjust.png'))

flick_to(Template('../../../Design/FaultDiag_DeleteUnit.png'), [1238, 321], DIR_UP, step=1, speed=SPEED_NORMAL)

sleep(2)

touch(Template('../../../Design/FaultDiag_DeleteUnit.png'))

touch(Template('../../../Design/FaultDiag_Delete_Confirm.png'))

try:
    assert_exists(Template('../../../Design/FaultDiag_DeleteUnit.png'))
    assert_not_exists(Template('../../../Design/FaultDiag_DeleteUnit_Select.png'))
except:
    error('Delete Unit History Error!')
