from autost.api import *

do_segment(Segment('../../Common/BackHomeView.tcs'))

try:
    assert_exists(Template('../../Design/Radio_Local_Card.png'))
except:
    error('LocalRadio Card Check Error!')
