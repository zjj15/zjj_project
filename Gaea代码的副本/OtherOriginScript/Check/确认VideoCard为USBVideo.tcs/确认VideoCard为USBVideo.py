from autost.api import *

do_segment(Segment('../../Common/BackHomeView.tcs'))

flick_to(Template('../../Design/Video_Picture_Card.png'), [972, 347], DIR_LEFT, step=1, speed=SPEED_NORMAL)

try:
    assert_exists(Template('../../Design/USB_Video_Card.png'))
except:
    error('USBVideo Card Check Error!')
