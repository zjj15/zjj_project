from autost.api import *

DEV1 = ST.DEV1
media_step = get_param('step')
if None == media_step:
    print('media_step is needed!')

print('Check：设定多媒体音量[step%s]' % media_step)
try:
    if media_step >= 0 and media_step <= 40:
        assert_exists(Template("../../../Design/check_media_volume_step%s.png" % media_step),device=DEV1, timeout=4, threshold=0.8)
    else:
        print('do nothing')
except:
    error('check Media_VolumeSetting_Slices/step%s error' % media_step)
