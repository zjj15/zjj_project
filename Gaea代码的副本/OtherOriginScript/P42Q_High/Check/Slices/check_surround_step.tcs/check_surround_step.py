from autost.api import *

###机型：P42Q High
###外设：Bose Amp

DEV1 = ST.DEV1
surround_step = get_param('step')
if None == surround_step:
    print('surround_step is needed!')

flick_to(Template('../../../Design/SoundEffect_SURROUND_title.png'), [649, 409], DIR_DOWN)

print('Check:环绕音SURROUND VOL %s' % surround_step)

if exists(Template('pic/capture_20210910163526114690.png')):
    poco('android.widget.ImageView', pos=(0.9104166666666667, 0.5916666666666667)).click()
else:
    pass

try:
    if surround_step >= -5 and surround_step < 0:
        assert_exists(Template("../../../Design/check_SE_SURROUND_VOL_m%s.png" % abs(surround_step)),device=DEV1, timeout=4, threshold=0.85)    
    elif surround_step >= 0 and surround_step <= 5:
        assert_exists(Template("../../../Design/check_SE_SURROUND_VOL_%s.png" % surround_step),device=DEV1, timeout=4, threshold=0.85)
    else:
        print('do nothing')
except:
    error('[P42Q_High] Check SURROUND/step%s error' % surround_step)
