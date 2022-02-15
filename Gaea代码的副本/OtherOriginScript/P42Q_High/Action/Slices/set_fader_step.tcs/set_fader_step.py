from autost.api import *


###机型：P42Q High
###外设：Bose Amp
dict_fader_step ={
    0: ST.P42Q_H_FADER_0,
    1: ST.P42Q_H_FADER_1,
    -1: ST.P42Q_H_FADER_m1,
    2: ST.P42Q_H_FADER_2,
    -2: ST.P42Q_H_FADER_m2,
    3: ST.P42Q_H_FADER_3,
    -3: ST.P42Q_H_FADER_m3,
    4: ST.P42Q_H_FADER_4,
    -4: ST.P42Q_H_FADER_m4,
    5: ST.P42Q_H_FADER_5,
    -5: ST.P42Q_H_FADER_m5
}
DEV1 = ST.DEV1
fader_step = get_param('step')
if None == fader_step:
    print('fader_step is needed!')

print('Item Action：前后平衡FADER[step%s]' % fader_step)
DEV1 = ST.DEV1
flick([660, 600], DIR_UP, step=1, speed=SPEED_NORMAL,device=DEV1)
flick([660, 600], DIR_UP, step=1, speed=SPEED_NORMAL,device=DEV1)

#Item Action：设定前后平衡FADER[-1]
touch([ST.P42Q_H_BALANCE_0,dict_fader_step[fader_step]],device=DEV1)
touch([ST.P42Q_H_BALANCE_0,dict_fader_step[fader_step]],device=DEV1)

try:
    if fader_step >= -5 and fader_step < 0:
        assert_exists(Template("../../../Design/check_SE_FADER_m%s.png" % abs(fader_step)),device=DEV1, timeout=4)    
    elif fader_step >= 0 and fader_step <= 5:
        assert_exists(Template("../../../Design/check_SE_FADER_%s.png" % fader_step),device=DEV1, timeout=4)
    else:
        print('do nothing')

except:
    error('[P42Q_High]SoundEffect/FADER/step%s setting error' % fader_step)
