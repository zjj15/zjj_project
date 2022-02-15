from autost.api import *

###机型：P42Q High
###外设：Bose Amp

DEV1 = ST.DEV1
fader_step = get_param('step')
if None == fader_step:
    print('fader_step is needed!')
flick([660, 600], DIR_UP, step=1, speed=SPEED_NORMAL,device=DEV1)
flick([660, 600], DIR_UP, step=1, speed=SPEED_NORMAL,device=DEV1)

#Check:前后平衡FADER[-1]
print('#Check:前后平衡FADER[%s]'% fader_step)
try:
    if fader_step >= -5 and fader_step < 0:
        assert_exists(Template("../../../Design/check_SE_FADER_m%s.png" % abs(fader_step)),device=DEV1, timeout=4, threshold=0.82)    
    elif fader_step >= 0 and fader_step <= 5:
        assert_exists(Template("../../../Design/check_SE_FADER_%s.png" % fader_step),device=DEV1, timeout=4, threshold=0.82)
    else:
        print('do nothing')
except:
    error('[P42Q_High] Check SoundEffect/FADER/step%s error' % fader_step)

