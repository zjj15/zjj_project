from autost.api import *

DEV1 = ST.DEV1
phone_step = get_param('step')
if None == phone_step:
    print('phone_step is needed!')

print('Check:电话音量[step%s]' % phone_step)
try:
    if phone_step >= 1 and phone_step <= 31:
        assert_exists(Template("../../../Design/check_VS_Phone_Volume_%s.png" % phone_step),device=DEV1, timeout=4, threshold=0.8)
    else:
        print('do nothing')
except:
    error('check PhoneVolumeSetting_Slices/step%s error' % phone_step)
