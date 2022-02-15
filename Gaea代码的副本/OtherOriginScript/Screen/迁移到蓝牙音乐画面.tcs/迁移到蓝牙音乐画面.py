from autost.api import *

do_segment(Segment('../../Common/BackHomeView.tcs'))

flick_to(Template('../../Design/Music_Card.png'), [971, 353], DIR_LEFT, step=1, speed=SPEED_NORMAL)

touch(Template('../../Design/Music_Card.png'))

#poco('蓝牙音乐', text='蓝牙音乐', timeout=4).click()
touch_or(Template('../../Design/BTAudio_button_no_focus.png'), Template('../../Design/BTAudio_button_focus.png'), threshold=0.90, timeout=5)

try:
    assert_exists(Template('../../Design/Equipment_management.png'), timeout=5)
    assert_exists(Template('../../Design/Prev_button.png'), timeout=5)
    assert_exists(Template('../../Design/BTA_Source.png'), timeout=5)
except:
    error('IntoBTA Error!')


 
