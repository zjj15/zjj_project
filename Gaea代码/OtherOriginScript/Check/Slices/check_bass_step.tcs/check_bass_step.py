from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

bass_step = get_param('step')
if None == bass_step:
    print('bass_step is needed!')
flick([660, 600], DIR_UP, step=1, speed=SPEED_NORMAL,device=DEV1)
flick([660, 600], DIR_UP, step=1, speed=SPEED_NORMAL,device=DEV1)

#Item Action：设定低音BASS[X]
print('Item Action：设定低音BASS[%s]'% bass_step)
try:
    if bass_step >= -5 and bass_step < 0:
        assert_exists(Template("../../../Design/check_SoundEffect_BASS_m%s.png" % abs(bass_step)),device=DEV1, timeout=4, threshold=0.8)    
    elif bass_step >= 0 and bass_step <= 5:
        assert_exists(Template("../../../Design/check_SoundEffect_BASS_%s.png" % bass_step),device=DEV1, timeout=4, threshold=0.8)
    else:
        print('do nothing')

except:
    error('Slices/check_bass_step step:%s setting error' % bass_step)
