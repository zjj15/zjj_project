from autost.api import *

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

do_segment(Segment('../迁移到蓝牙电话画面.tcs'))

touch(Template('../../Design/BTHF_ShortBar_Contact_nofocus.png'),threshold = 0.8)
sleep(2)
ST.BTHF_Contact = 'BTHF_Contact.png'
snapshot(rect=[205, 221, 1534, 459], filename=os.path.join(ST.LOG_DIR, ST.BTHF_Contact))

try:
    wait_for_appearance(Template('../../Design/BTHF_Contact_Refresh.png'), timeout=100)
    #assert_exists(Template('../../Design/BTHF_Contact_Refresh.png'))
    assert_exists(Template('../../Design/BTHF_Contact_Search_Input.png'))
except:
    error('IntoBTHF Contact Error!')
