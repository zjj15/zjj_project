from autost.api import *
###机型：P42Q High
###外设：Bose Amp
dict_surround_step ={
    0: ST.P42Q_H_SURROUND_0,
    1: ST.P42Q_H_SURROUND_1,
    -1: ST.P42Q_H_SURROUND_m1,
    2: ST.P42Q_H_SURROUND_2,
    -2: ST.P42Q_H_SURROUND_m2,
    3: ST.P42Q_H_SURROUND_3,
    -3: ST.P42Q_H_SURROUND_m3,
    4: ST.P42Q_H_SURROUND_4,
    -4: ST.P42Q_H_SURROUND_m4,
    5: ST.P42Q_H_SURROUND_5,
    -5: ST.P42Q_H_SURROUND_m5
}

DEV1 = ST.DEV1
surround_step = get_param('step')
if None == surround_step:
    print('surround_step is needed!')

#前置条件
##画面Touch位置Top为准
flick_to(Template('../../../Design/check_SE_BoseEffect_title.png'), [649, 409], DIR_DOWN)

##环绕音mode：ON
do_segment(Segment('../../设定_音效SURROUND MODE设置为ON[M-CAN Bose].tcs'))


print('Item Action：设定环绕音SURROUND VOL[step%s]' % surround_step)
try:
    if(exists(Template('../../../Design/SoundEffect_SURROUND_title.png'),device=DEV1, timeout=4)):
        touch(dict_surround_step[surround_step],device=DEV1)
        touch(dict_surround_step[surround_step],device=DEV1)
    if surround_step >= -5 and surround_step < 0:
        assert_exists(Template("../../../Design/check_SE_SURROUND_VOL_m%s.png" % abs(surround_step)),device=DEV1, timeout=4)    
    elif surround_step >= 0 and surround_step <= 5:
        assert_exists(Template("../../../Design/check_SE_SURROUND_VOL_%s.png" % surround_step),device=DEV1, timeout=4)
    else:
        print('do nothing')

except:
    error('[P42Q_High SoundEffect_surround step%s setting error' % surround_step)
