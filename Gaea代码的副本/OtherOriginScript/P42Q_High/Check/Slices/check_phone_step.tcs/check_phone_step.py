from autost.api import *

###机型：P42Q High
###外设：Bose Amp

DEV1 = ST.DEV1
phone_step = get_param('step')
if None == phone_step:
    print('phone_step is needed!')

print('Check:电话音量[step%s]' % phone_step)
try:
    if phone_step >= 5 and phone_step <= 40:
        assert_exists(Template("../../../Design/check_VS_Phone_Volume_%s.png" % phone_step),device=DEV1, timeout=4)
    else:
        print('do nothing')
except:
    error('[P42Q_High]check PhoneVolumeSetting_Slices/step%s error' % phone_step)
