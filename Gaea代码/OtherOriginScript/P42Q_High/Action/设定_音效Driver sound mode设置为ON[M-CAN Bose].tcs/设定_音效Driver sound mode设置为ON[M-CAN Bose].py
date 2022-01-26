from autost.api import *

###机型：P42Q High
###外设：Bose Amp

DEV1 = ST.DEV1

flick([660, 600], DIR_UP, step=1, speed=SPEED_NORMAL,device=DEV1)
flick([660, 600], DIR_UP, step=1, speed=SPEED_NORMAL,device=DEV1)

#Item Action：设定主驾模式[ON]

touch_if(Template('../../../Design/check_SE_DriveSound_Mode_off.png'),device=DEV1, timeout=4, threshold=0.85)

try:
    assert_exists(Template("../../../Design/check_SE_DriveSound_Mode_on.png"),device=DEV1, timeout=4, threshold=0.85)

except:
    error('[P42Q_High]SoundEffect/SURROUND/MODE Set_ON error')
