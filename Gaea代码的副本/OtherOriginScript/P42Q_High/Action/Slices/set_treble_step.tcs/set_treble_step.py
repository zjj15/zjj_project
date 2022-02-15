from autost.api import *
###机型：P42Q High
###外设：Bose Amp

dict_treble_step ={
    0: ST.P42Q_H_TREBLE_step0_Point,
    1: ST.P42Q_H_TREBLE_step1_Point,
    -1: ST.P42Q_H_TREBLE_step_minus1_Point,
    2: ST.P42Q_H_TREBLE_step2_Point,
    -2: ST.P42Q_H_TREBLE_step_minus2_Point,
    3: ST.P42Q_H_TREBLE_step3_Point,
    -3: ST.P42Q_H_TREBLE_step_minus3_Point,
    4: ST.P42Q_H_TREBLE_step4_Point,
    -4: ST.P42Q_H_TREBLE_step_minus4_Point,
    5: ST.P42Q_H_TREBLE_step5_Point,
    -5: ST.P42Q_H_TREBLE_step_minus5_Point,
    6: ST.P42Q_H_TREBLE_step6_Point,
    -6: ST.P42Q_H_TREBLE_step_minus6_Point,
    7: ST.P42Q_H_TREBLE_step7_Point,
    -7: ST.P42Q_H_TREBLE_step_minus7_Point,
    8: ST.P42Q_H_TREBLE_step8_Point,
    -8: ST.P42Q_H_TREBLE_step_minus8_Point,
    9: ST.P42Q_H_TREBLE_step9_Point,
    -9: ST.P42Q_H_TREBLE_step_minus9_Point
}

DEV1 = ST.DEV1
treble_step = get_param('step')
if None == treble_step:
    print('treble_step is needed!')

#Item Action：设定低音BASS[-1]
try:
    if(exists(Template("../../../Design/SoundEffect_TREBLE_title.png"),device=DEV1, timeout=4)):
        touch(dict_treble_step[treble_step],device=DEV1)
    if treble_step >= -9 and treble_step < 0:
        assert_exists(Template("../../../Design/check_SoundEffect_TREBLE_m%s.png" % abs(treble_step)),device=DEV1, timeout=4)
    elif treble_step >= 0 and treble_step <= 9:
        assert_exists(Template("../../../Design/check_SoundEffect_TREBLE_%s.png" % treble_step),device=DEV1, timeout=4)

except:
    error('SoundEffect/step%s setting error' % treble_step)
