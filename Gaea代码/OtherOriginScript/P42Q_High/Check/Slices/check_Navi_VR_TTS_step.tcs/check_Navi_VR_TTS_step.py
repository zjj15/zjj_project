from autost.api import *

###机型：P42Q High
###外设：Bose Amp

DEV1 = ST.DEV1
navi_vr_tts_step = get_param('step')
if None == navi_vr_tts_step:
    print('navi_vr_tts_step is needed!')

print('Check:导航和语音音量[step%s]' % navi_vr_tts_step)
try:
    if navi_vr_tts_step >= 5 and navi_vr_tts_step <= 40:
        assert_exists(Template("../../../Design/check_VS_Navi_VR_TTS_Volume_%s.png" % navi_vr_tts_step),device=DEV1, timeout=4)
    else:
        print('do nothing')
except:
    error('[P42Q_High]check Navi_VR_TTS VolumeSetting step%s error' % navi_vr_tts_step)
