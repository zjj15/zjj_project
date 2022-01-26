from autost.api import *

def outgoing():
    #call 10086
    touch(Template('../../Design/BTHF_Keyboard_1.png'))
    touch(Template('../../Design/BTHF_Keyboard_0.png'))
    touch(Template('../../Design/BTHF_Keyboard_0.png'))
    touch(Template('../../Design/BTHF_Keyboard_8.png'))
    touch(Template('../../Design/BTHF_Keyboard_6.png'))
    touch(Template('../../Design/BTHF_Keyboard_Outgoing.png'))

touch_if(Template('../../Design/BTHF_ShortBar_Keyboard_nofocus.png'), timeout=2)

outgoing()
sleep(2)

try:
    assert_exists(Template('../../Design/BTHF_Outgoing_Screen.png'))
except:
    error('BTHF_Outgoing Error!')

touch(Template('../../Design/BTHF_Outing_HangUp.png'))

 





