from autost.api import *

from autost.api import *

DEV1 = ST.DEV1
 
#前置条件
##打开USB
do_segment(Segment("../openUSB_all.tcs"))

#Configuration varies
do_segment(Segment("../../Screen/进入Fault diagnosis.tcs"))

touch(Template('../../Design/FaultDiag_Comfirm_Adjust.png'),device=DEV1)

flick([1432, 553], DIR_UP, step=3, speed=SPEED_NORMAL)

touch_if(Template('../../Design/FaultDiag_ConfigFileUpdate.png'),device=DEV1, timeout=4)

if exists(Template('../../Design/FaultDiag_ConfigFile_nofile_message.png'),device=DEV1, timeout=4):
    touch(Template("../../Design/FaultDiag_ConfigFile_nofind_Check.png"))
    error('Config File Update Error:No Update file detected.')
try:
    if exists(Template('../../Design/FaultDiag_ConfigFile_ModelSelect.png'),device=DEV1, timeout=4):
        flick([906, 525], DIR_UP, step=2, speed=SPEED_NORMAL,device=DEV1)
        touch(Template('../../Design/FaultDiag_ConfigFile_Update_MidLow_optTC.png'),device=DEV1, threshold=0.89, timeout=2)
        touch(Template('../../Design/FaultDiag_ConfigFile_Update_check.png'),device=DEV1)
        if exists(Template('../../Design/FaultDiag_ConfigFile_Update_Succeed.png'),device=DEV1, timeout=6):
            touch(Template('../../Design/FaultDiag_ConfigFile_Update_Succeed_Check.png'),device=DEV1)
            sleep(30)
        
except:
    error('Config File Update:Failed! ')
