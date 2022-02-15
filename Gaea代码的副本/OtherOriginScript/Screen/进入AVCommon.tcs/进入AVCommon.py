from autost.api import *

touch(Template('../../Design/FaultDiag_Comfirm_Adjust.png'))

touch(Template('../../Design/FaultDiag_AVComm.png'))
sleep(1)
ST.avcommon = 'avcommon.png'
snapshot(rect=[456, 142, 1011, 507], filename=os.path.join(ST.LOG_DIR, ST.avcommon))

try:
    assert_exists(Template('../../Design/FaultDiag_AVComm_Reset.png'))
except:
    error('Into AVCommon Error!')
