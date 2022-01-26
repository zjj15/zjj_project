from autost.api import *

do_segment(Segment('../../../Common/BackHomeView.tcs'))

try:
    assert_exists(Template('pic/capture_20210208111648088362.png'))
except:
    error('Last Source Chcek init Error!')