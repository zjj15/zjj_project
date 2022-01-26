from autost.api import *

DialPhoneName = 'A_MB_0107'
DialPhoneDeviceNo = 'iAndroid://127.0.0.1:5037/DRGGAM0860501882'

for i in range(2):
    touch_if(Template('../../../Design/Phone_A_MB_0107/StatusBar_btcalling_icon.png'), timeout=3, threshold=0.85, device=DialPhoneDeviceNo)

    if exists(Template('../../../Design/Phone_A_MB_0107/Outgoing_1.png'), timeout=1, device=DialPhoneDeviceNo):
        touch(Template('../../../Design/Phone_A_MB_0107/Outgoing_1.png'), device=DialPhoneDeviceNo)
        break
    elif exists(Template('../../../Design/Phone_A_MB_0107/Outgoing_2.png'), timeout=1, device=DialPhoneDeviceNo):
        touch(Template('../../../Design/Phone_A_MB_0107/Outgoing_2.png'), device=DialPhoneDeviceNo)
        break
    else:
        sleep(1)
sleep(2)
