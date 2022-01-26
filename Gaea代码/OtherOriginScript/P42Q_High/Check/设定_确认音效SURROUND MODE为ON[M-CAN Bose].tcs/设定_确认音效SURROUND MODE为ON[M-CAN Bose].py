from autost.api import *

###机型：P42Q High
###外设：Bose Amp

DEV1 = ST.DEV1

#Check：环绕音[OFF]
try:
    assert_exists(Template('../../../Design/check_SE_SURROUND_Mode_on.png'),device=DEV1, timeout=4, threshold=0.85)

except:
    error('[P42Q_High] Check SoundEffect/M_CAN_Bose_Amp/SURROUND/MODE Set_OFF error')

