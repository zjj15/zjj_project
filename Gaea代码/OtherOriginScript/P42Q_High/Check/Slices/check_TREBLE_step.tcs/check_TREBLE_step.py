from autost.api import *

###机型：P42Q High
###外设：Bose Amp

DEV1 = ST.DEV1
treble_step = get_param('step')
if None == treble_step:
    print('treble_step is needed!')

print('Check:TREBLE %s' % treble_step)
try:
    if treble_step >= -9 and treble_step < 0:
        assert_exists(Template("../../../Design/check_SoundEffect_TREBLE_m%s.png" % abs(treble_step)),device=DEV1, timeout=4)    
    elif treble_step >= 0 and treble_step <= 9:
        assert_exists(Template("../../../Design/check_SoundEffect_TREBLE_%s.png" % treble_step),device=DEV1, timeout=4)
    else:
        print('do nothing')
except:
    error('[P42Q_High] Check TREBLE/step%s error' % treble_step)
