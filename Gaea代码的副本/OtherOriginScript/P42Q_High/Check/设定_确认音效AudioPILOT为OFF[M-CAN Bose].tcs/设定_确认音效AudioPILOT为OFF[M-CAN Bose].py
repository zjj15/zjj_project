from autost.api import *

###机型：P42Q High
###外设：Bose Amp

DEV1 = ST.DEV1

#Check：噪音补偿[OFF]
try:
    assert_exists(Template("../../../Design/check_SE_AudioPILOT_off.png"),device=DEV1, timeout=4, threshold=0.70,ignore_bg=True)
except:
    error('[P42Q_High] Check SoundEffect/M_CAN_Bose_Amp/AudioPILOT/OFF error')
