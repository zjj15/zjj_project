from autost.api import *
dict_set_balance_step ={
    0: ST.P42Q_BALANCE_0,
    1: ST.P42Q_BALANCE_1,
    -1: ST.P42Q_BALANCE_m1,
    2: ST.P42Q_BALANCE_2,
    -2: ST.P42Q_BALANCE_m2,
    3: ST.P42Q_BALANCE_3,
    -3: ST.P42Q_BALANCE_m3,
    4: ST.P42Q_BALANCE_4,
    -4: ST.P42Q_BALANCE_m4,
    5: ST.P42Q_BALANCE_5,
    -5: ST.P42Q_BALANCE_m5
}

DEV1 = ST.DEV1
balance_step = get_param('step')
if None == balance_step:
    print('balance_step is needed!')

flick([660, 600], DIR_UP, step=1, speed=SPEED_NORMAL,device=DEV1)
flick([660, 600], DIR_UP, step=1, speed=SPEED_NORMAL,device=DEV1)

print('Item Action：左右平衡BALANCE[step%s]' % balance_step)

touch([dict_set_balance_step[balance_step],ST.P42Q_FADER_0],device=DEV1)
touch([dict_set_balance_step[balance_step],ST.P42Q_FADER_0],device=DEV1)

try:
    if balance_step >= -5 and balance_step < 0:
        assert_exists(Template("../../../Design/check_SE_BALANCE_m%s.png" % abs(balance_step)),device=DEV1, timeout=4) 
    elif balance_step >= 0 and balance_step <= 5:
        assert_exists(Template("../../../Design/check_SE_BALANCE_%s.png" % balance_step),device=DEV1, timeout=4)
    else:
        print('do nothing')

except:
    error('SoundEffect/BALANCE/step%s setting error' % balance_step)