from autost.api import *

do_segment(Segment('../../Common/BackHomeView.tcs'))

flick_to(Template('../../Design/BTHF_Card.png'), [968, 397], DIR_LEFT, step=1, speed=SPEED_NORMAL)

for i in range(3):
    if exists(Template('../../Design/BTHF_Card.png'), timeout = 1):
        touch(Template('../../Design/BTHF_Card.png'))
        sleep(1)
    else:
        break

touch_if(Template('../../Design/BTHF_ShortBar_Keyboard_nofocus.png'), timeout=2)

ST.BTHF_Records = 'BTHF_Records.png'
snapshot(rect=[819, 139, 1020, 544], filename=os.path.join(ST.LOG_DIR, ST.BTHF_Records))

try:
    assert_exists(Template('../../Design/ShortBar_BTHF_focus.png'))
except:
    error('IntoBTHF error!')
