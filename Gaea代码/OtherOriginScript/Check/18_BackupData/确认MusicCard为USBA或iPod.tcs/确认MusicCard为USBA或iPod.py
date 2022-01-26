from autost.api import *

do_segment(Segment('../../../Common/BackHomeView.tcs'))

flick_to(Template('../../../Design/Music_Card.png'), [971, 353], DIR_LEFT, step=1, speed=SPEED_NORMAL)

touch(Template('../../../Design/Music_Card.png'))

touch([69, 404])

try:
    assert_exists(Template(os.path.join(ST.LOG_DIR, ST.audio_usboriPod)))
except:
    error('Last USB Source Keep Check Error!')