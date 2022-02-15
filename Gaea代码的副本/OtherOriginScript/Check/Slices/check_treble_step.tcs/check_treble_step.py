from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

trible_step = get_param('step')
if None == trible_step:
    print('trible_step is needed!')
flick([660, 600], DIR_UP, step=1, speed=SPEED_NORMAL,device=DEV1)
flick([660, 600], DIR_UP, step=1, speed=SPEED_NORMAL,device=DEV1)


#Item Action：设定低音TREBLE[X]
print('Item Action：设定低音TREBLE[%s]'% trible_step)

try:
    if trible_step >= -5 and trible_step < 0:
        assert_exists(Template("../../../Design/check_SoundEffect_TREBLE_m%s.png" % abs(trible_step)),device=DEV1, timeout=4, threshold=0.8)    
    elif trible_step >= 0 and trible_step <= 5:
        assert_exists(Template("../../../Design/check_SoundEffect_TREBLE_%s.png" % trible_step),device=DEV1, timeout=4, threshold=0.8)
    else:
        print('do nothing')
except:
    error('Slices/check_trible_step step:%s setting error' % trible_step)
