from autost.api import *

do_segment(Segment('../../Common/BackHomeView.tcs'))

try:
    assert_exists(Template('../../Design/NissanRadio_Card_Check.png'))
except:
    error('NissanRadio Card Check Error!')
