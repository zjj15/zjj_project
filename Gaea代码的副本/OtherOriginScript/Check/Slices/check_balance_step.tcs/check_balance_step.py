from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

balance_step = get_param('step')
if None == balance_step:
    print('balance_step is needed!')
flick([660, 600], DIR_UP, step=1, speed=SPEED_NORMAL,device=DEV1)
flick([660, 600], DIR_UP, step=1, speed=SPEED_NORMAL,device=DEV1)


#Item Action：Check左右平衡BALANCE[X]
print('Item Action：Check左右平衡BALANCE[%s]'% balance_step)

try:
    if balance_step >= -5 and balance_step < 0:
        assert_exists(Template('../../../Design/check_SE_BALANCE_m%s.png' % abs(balance_step)),device=DEV1, timeout=4, threshold=0.8)    
    elif balance_step >= 0 and balance_step <= 5:
        assert_exists(Template('../../../Design/check_SE_BALANCE_%s.png' % balance_step),device=DEV1, timeout=4, threshold=0.8)
    else:
        print('do nothing')
except:
    error('Slices/check_balance_step step:%s setting error' % balance_step)
