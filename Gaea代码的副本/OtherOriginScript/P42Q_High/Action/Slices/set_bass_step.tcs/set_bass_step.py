from autost.api import *
dict_bass_step ={
    0: ST.P42Q_H_BASS_step0_Point,
    1: ST.P42Q_H_BASS_step1_Point,
    -1: ST.P42Q_H_BASS_step_minus1_Point,
    2: ST.P42Q_H_BASS_step2_Point,
    -2: ST.P42Q_H_BASS_step_minus2_Point,
    3: ST.P42Q_H_BASS_step3_Point,
    -3: ST.P42Q_H_BASS_step_minus3_Point,
    4: ST.P42Q_H_BASS_step4_Point,
    -4: ST.P42Q_H_BASS_step_minus4_Point,
    5: ST.P42Q_H_BASS_step5_Point,
    -5: ST.P42Q_H_BASS_step_minus5_Point,
    6: ST.P42Q_H_BASS_step6_Point,
    -6: ST.P42Q_H_BASS_step_minus6_Point,
    7: ST.P42Q_H_BASS_step7_Point,
    -7: ST.P42Q_H_BASS_step_minus7_Point,
    8: ST.P42Q_H_BASS_step8_Point,
    -8: ST.P42Q_H_BASS_step_minus8_Point,
    9: ST.P42Q_H_BASS_step9_Point,
    -9: ST.P42Q_H_BASS_step_minus9_Point,
}
###机型：P42Q High
###外设：Bose Amp

DEV1 = ST.DEV1
bass_step = get_param('step')
if None == bass_step:
    print('bass_step is needed!')

#Item Action：设定低音BASS
try:
    if(exists(Template('../../../Design/SoundEffect_BASS_title.png'),device=DEV1, timeout=4)):
        touch(dict_bass_step[bass_step],device=DEV1)
        touch(dict_bass_step[bass_step],device=DEV1)
    if bass_step >= -9 and bass_step < 0:
        assert_exists(Template("../../../Design/check_SoundEffect_BASS_m%s.png" % abs(bass_step)),device=DEV1, timeout=4, threshold=0.95)
    elif bass_step >= 0 and bass_step <= 9:
        assert_exists(Template("../../../Design/check_SoundEffect_BASS_%s.png" % bass_step),device=DEV1, timeout=4, threshold=0.95)
except:
    error('[P42Q_High]SoundEffect/step%s setting error' % bass_step)
