from autost.api import *


###机型：P42Q High
###外设：Bose Amp

DEV1 = ST.DEV1
swipe([1450,200],[1450,400])
#Item Action：设定环绕音[ON]
if exists(Template('../../../Design/check_SE_SURROUND_Mode_off.png'),device=DEV1, timeout=4, threshold=0.85):
    touch(ST.P42Q_H_SURROUND_MODE_SetOFF_Point,device=DEV1)
else:
    pass

try:
    assert_exists(Template('../../../Design/check_SE_SURROUND_Mode_on.png'),device=DEV1, timeout=4, threshold=0.85)

except:
    error('[P42Q_High]SoundEffect/SURROUND/MODE Set_ON error')
