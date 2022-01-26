from autost.api import *

dict_Navi_VR_TTS_Volume_step = {
    1: ST.Navi_VR_TTS_Volume_step1_Point,
    2: ST.Navi_VR_TTS_Volume_step2_Point,
    3: ST.Navi_VR_TTS_Volume_step3_Point,
    4: ST.Navi_VR_TTS_Volume_step4_Point,
    5: ST.Navi_VR_TTS_Volume_step5_Point,
    6: ST.Navi_VR_TTS_Volume_step6_Point,
    7: ST.Navi_VR_TTS_Volume_step7_Point,
    8: ST.Navi_VR_TTS_Volume_step8_Point,
    9: ST.Navi_VR_TTS_Volume_step9_Point,
    10: ST.Navi_VR_TTS_Volume_step10_Point,
    11: ST.Navi_VR_TTS_Volume_step11_Point,
    12: ST.Navi_VR_TTS_Volume_step12_Point
}

DEV1 = ST.DEV1

navi_vr_tts_step = get_param('step')
if None == navi_vr_tts_step:
    print('navi_vr_tts_step is needed!')

#Item Action：设定导航和语音音量[step1]
print('Item Action：设定导航和语音音量[step%s]' % navi_vr_tts_step )

try:
    if(exists(Template('../../../Design/Navi_VR_TTS_Volume_Tiltle.png'),device=DEV1, timeout=4)):
         touch(dict_Navi_VR_TTS_Volume_step[navi_vr_tts_step],device=DEV1)
    assert_exists(Template("../../../Design/check_Navi_VR_TTS_step%s.png" % navi_vr_tts_step),device=DEV1, timeout=4)
except:
    error('Slices/Navi_VR_TTS_step step:%s setting error' % navi_vr_tts_step)
