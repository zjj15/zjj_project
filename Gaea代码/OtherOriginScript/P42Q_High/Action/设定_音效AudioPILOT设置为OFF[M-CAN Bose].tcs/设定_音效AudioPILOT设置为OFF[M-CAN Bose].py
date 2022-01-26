from autost.api import *

###机型：P42Q High
###外设：Bose Amp

DEV1 = ST.DEV1

#Item Action：设定噪音补偿[OFF]
if exists(Template('../../../Design/check_SE_AudioPILOT_on.png'),device=DEV1, timeout=4, threshold=0.70):
    touch(ST.P42Q_H_AudioPILOT_SetPoint,device=DEV1)

try:
    assert_exists(Template('../../../Design/check_SE_AudioPILOT_off.png'),device=DEV1, timeout=4, threshold=0.70)
except:
    error('[P42Q_High]SoundEffect/AudioPILOT/ Set_OFF error')

