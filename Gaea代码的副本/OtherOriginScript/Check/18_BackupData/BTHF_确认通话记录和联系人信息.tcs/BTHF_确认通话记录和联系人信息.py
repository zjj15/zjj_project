from autost.api import *

try:
    assert_exists(Template(os.path.join(ST.LOG_DIR, ST.BTHF_Contact)))
    touch_if(Template('../../../Design/BTHF_ShortBar_Keyboard_nofocus.png'), timeout=2)
    do_segment(Segment("../../../screen/迁移到蓝牙电话画面.tcs"))
    assert_exists(Template(os.path.join(ST.LOG_DIR, ST.BTHF_Records)))
except:
    error('BTHF Contact Records Check Error!')
