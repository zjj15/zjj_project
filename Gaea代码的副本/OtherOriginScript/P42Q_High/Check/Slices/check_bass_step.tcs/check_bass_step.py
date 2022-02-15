from autost.api import *


###机型：P42Q High
###外设：Bose Amp

DEV1 = ST.DEV1

bass_step = get_param('step')
if None == bass_step:
    print('bass_step is needed!')

print('check：低音BASS[%s]'% bass_step)
try:
    if bass_step >= -9 and bass_step < 0:
        assert_exists(Template("../../../Design/check_SoundEffect_BASS_m%s.png" % abs(bass_step)),device=DEV1, timeout=4)    
    elif bass_step >= 0 and bass_step <= 9:
        assert_exists(Template("../../../Design/check_SoundEffect_BASS_%s.png" % bass_step),device=DEV1, timeout=4)
    else:
        print('do nothing')

except:
    error('[P42Q_High] Slices/check_bass_step step:%s setting error' % bass_step)
