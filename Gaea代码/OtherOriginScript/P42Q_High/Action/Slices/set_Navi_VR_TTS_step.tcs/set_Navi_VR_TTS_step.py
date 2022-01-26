from autost.api import *

###机型：P42Q High
###外设：Bose Amp

dict_Navi_VR_TTS_Volume_step = {
    10: ST.P42Q_H_Navi_VR_TTS_Volume_step10_Point,
    11: ST.P42Q_H_Navi_VR_TTS_Volume_step11_Point,
    12: ST.P42Q_H_Navi_VR_TTS_Volume_step12_Point,
    13: ST.P42Q_H_Navi_VR_TTS_Volume_step13_Point,
    14: ST.P42Q_H_Navi_VR_TTS_Volume_step14_Point,
    15: ST.P42Q_H_Navi_VR_TTS_Volume_step15_Point,
    16: ST.P42Q_H_Navi_VR_TTS_Volume_step16_Point,
    17: ST.P42Q_H_Navi_VR_TTS_Volume_step17_Point,
    18: ST.P42Q_H_Navi_VR_TTS_Volume_step18_Point,
    19: ST.P42Q_H_Navi_VR_TTS_Volume_step19_Point,
    20: ST.P42Q_H_Navi_VR_TTS_Volume_step20_Point,
    21: ST.P42Q_H_Navi_VR_TTS_Volume_step21_Point,
    22: ST.P42Q_H_Navi_VR_TTS_Volume_step22_Point,
    23: ST.P42Q_H_Navi_VR_TTS_Volume_step23_Point,
    24: ST.P42Q_H_Navi_VR_TTS_Volume_step24_Point,
    25: ST.P42Q_H_Navi_VR_TTS_Volume_step25_Point,
    26: ST.P42Q_H_Navi_VR_TTS_Volume_step26_Point,
    27: ST.P42Q_H_Navi_VR_TTS_Volume_step27_Point,
    28: ST.P42Q_H_Navi_VR_TTS_Volume_step28_Point,
    29: ST.P42Q_H_Navi_VR_TTS_Volume_step29_Point,
    30: ST.P42Q_H_Navi_VR_TTS_Volume_step30_Point,
    31: ST.P42Q_H_Navi_VR_TTS_Volume_step31_Point,
    32: ST.P42Q_H_Navi_VR_TTS_Volume_step32_Point,
    33: ST.P42Q_H_Navi_VR_TTS_Volume_step33_Point,
    34: ST.P42Q_H_Navi_VR_TTS_Volume_step34_Point,
    35: ST.P42Q_H_Navi_VR_TTS_Volume_step35_Point,
    36: ST.P42Q_H_Navi_VR_TTS_Volume_step36_Point,
    37: ST.P42Q_H_Navi_VR_TTS_Volume_step37_Point,
    38: ST.P42Q_H_Navi_VR_TTS_Volume_step38_Point,
    39: ST.P42Q_H_Navi_VR_TTS_Volume_step39_Point,
    40: ST.P42Q_H_Navi_VR_TTS_Volume_step40_Point,
    5: ST.P42Q_H_Navi_VR_TTS_Volume_step5_Point,
    6: ST.P42Q_H_Navi_VR_TTS_Volume_step6_Point,
    7: ST.P42Q_H_Navi_VR_TTS_Volume_step7_Point,
    8: ST.P42Q_H_Navi_VR_TTS_Volume_step8_Point,
    9: ST.P42Q_H_Navi_VR_TTS_Volume_step9_Point
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
        touch(dict_Navi_VR_TTS_Volume_step[navi_vr_tts_step],device=DEV1)
        touch(dict_Navi_VR_TTS_Volume_step[navi_vr_tts_step],device=DEV1)
    assert_exists(Template("../../../Design/check_VS_Navi_VR_TTS_Volume_%s.png" % navi_vr_tts_step),device=DEV1, timeout=4)
except:
    error('[P42Q_High] Slices/Navi_VR_TTS_step step:%s setting error' % navi_vr_tts_step)
