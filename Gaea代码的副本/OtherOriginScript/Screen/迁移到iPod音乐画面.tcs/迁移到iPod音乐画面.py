from autost.api import *

do_segment(Segment('../../Common/BackHomeView.tcs'))

flick_to(Template('../../Design/Music_Card.png'), [971, 344], DIR_LEFT, step=1, speed=SPEED_NORMAL)

touch(Template('../../Design/Music_Card.png'))

do_segment(Segment('../../Action/USB_端口AllOFF.tcs'))
do_segment(Segment('../../Action/USB_端口2ON.tcs'))
sleep(5)

poco('iPod音乐', text='iPod音乐', timeout=4).click()

try:
    #assert_exists(Template('../../Design/ShortBar_iPod_focus.png'))
    assert_exists(Template('../../Design/iPod_Source.png'))
except:
    error('IntoiPod Error!')
