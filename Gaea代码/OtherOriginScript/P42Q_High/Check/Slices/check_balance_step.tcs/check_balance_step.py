from autost.api import *

###机型：P42Q High
###外设：Bose Amp

DEV1 = ST.DEV1
balance_step = get_param('step')
if None == balance_step:
    print('balance_step is needed!')

flick([660, 600], DIR_UP, step=1, speed=SPEED_NORMAL,device=DEV1)
flick([660, 600], DIR_UP, step=1, speed=SPEED_NORMAL,device=DEV1)


#Check:左右平衡BALANCE[X]
print('Check:左右平衡BALANCE[%s]'% balance_step)
try:
    if balance_step >= -5 and balance_step < 0:
        assert_exists(Template("../../../Design/check_SE_BALANCE_m%s.png" % abs(balance_step)),device=DEV1, timeout=4)
    elif balance_step >= 0 and balance_step <= 5:
        assert_exists(Template("../../../Design/check_SE_BALANCE_%s.png" % balance_step),device=DEV1, timeout=4)
    else:
        print('do nothing')
except:
    error('[P42Q_High] Check SoundEffect/BALANCE/step%s error' % balance_step)
