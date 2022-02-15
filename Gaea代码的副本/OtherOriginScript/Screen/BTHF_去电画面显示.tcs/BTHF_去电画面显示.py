from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
DEV2 = 'iAndroid://127.0.0.1:5037/DRGGAM0860501882'
#拨号手机
DialPhoneName = 'A_MB_0107'
DialPhoneDeviceNo = 'A_MB_0107://127.0.0.1:5037/DRGGAM0860501882'

DialNumber = get_param('phonenumber')
dict_dial_num = {
    '0':Template('../../Design/Phone_A_MB_0107/Diag_0.png'),
    '1':Template('../../Design/Phone_A_MB_0107/Diag_1.png'),
    '2':Template('../../Design/Phone_A_MB_0107/Diag_2.png'),
    '3':Template('../../Design/Phone_A_MB_0107/Diag_3.png'),
    '4':Template('../../Design/Phone_A_MB_0107/Diag_4.png'),
    '5':Template('../../Design/Phone_A_MB_0107/Diag_6.png'),
    '6':Template('../../Design/Phone_A_MB_0107/Diag_6.png'),
    '7':Template('../../Design/Phone_A_MB_0107/Diag_7.png'),
    '8':Template('../../Design/Phone_A_MB_0107/Diag_8.png'),
    '9':Template('../../Design/Phone_A_MB_0107/Diag_9.png')
}

def Phone_Outgoing():
    keyevent(HOME, device=DEV2)
    keyevent(HOME, device=DEV2)
    touch(Template('../../Design/Phone_Call_Card.png'), device=DEV2)
    #清除残留号码
    i=0
    while exists(Template('../../Design/Phone_A_MB_0107/DialDeleteBtn.png'), device=DEV2):
        touch(Template('../../Design/Phone_A_MB_0107/DialDeleteBtn.png'), device=DEV2)
        i += 1
        if i>20:
            break
    if DialNumber and 11==len(DialNumber):
        for i in DialNumber:
            touch(dict_dial_num[i], device=DEV2)
    else:
        #call 13918433497
        for i in '13918433497':
            touch(dict_dial_num[i], device=DEV2)
    touch(Template('../../Design/Phone_A_MB_0107/Diag_CallBegin.png'), device=DEV2)


do_segment(Segment('../../Common/BackHomeView.tcs'))
Phone_Outgoing()

try:
    assert_exists(Template('../../Design/statusbar_EndCallBtn.png'), device=DEV1)
except:
    error('BTHF_Incoming Error!')
