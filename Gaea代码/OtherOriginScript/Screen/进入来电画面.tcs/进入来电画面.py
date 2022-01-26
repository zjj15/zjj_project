from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
DEV2 = 'iAndroid://127.0.0.1:5037/031603b3f8141501'

def Phone_Outgoing():
    keyevent(HOME, device=DEV2)
    keyevent(HOME, device=DEV2)
    touch(Template('../../Design/Phone_Call_Card.png'), device=DEV2)
    #call 13918433497
    touch(Template('../../Design/Phone_Keyboard_1.png'), device=DEV2)
    touch(Template('../../Design/Phone_Keyboard_3.png'), device=DEV2)
    touch(Template('../../Design/Phone_Keyboard_9.png'), device=DEV2)
    touch(Template('../../Design/Phone_Keyboard_1.png'), device=DEV2)
    touch(Template('../../Design/Phone_Keyboard_8.png'), device=DEV2)
    touch(Template('../../Design/Phone_Keyboard_4.png'), device=DEV2)
    touch(Template('../../Design/Phone_Keyboard_3.png'), device=DEV2)
    touch(Template('../../Design/Phone_Keyboard_3.png'), device=DEV2)
    touch(Template('../../Design/Phone_Keyboard_4.png'), device=DEV2)
    touch(Template('../../Design/Phone_Keyboard_9.png'), device=DEV2)
    touch(Template('../../Design/Phone_Keyboard_7.png'), device=DEV2)
    touch(Template('../../Design/Phone_Keyboard_Outgoing.png'), device=DEV2)

do_segment(Segment('../../Common/BackHomeView.tcs'))

Phone_Outgoing()

try:
    assert_exists(Template('../../Design/BTHF_Incoming_Screen.png'), device=DEV1)
    assert_exists(Template('../../Design/BTHF_Incoming_Screen_II.png'), device=DEV1)
except:
    error('BTHF_Incoming Error!')

touch(Template('../../Design/Phone_Keyboard_HangUp.png'), device=DEV2)



