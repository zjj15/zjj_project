from autost.api import *

do_segment(Segment('../../Common/BackHomeView.tcs'))

assert_exists(Template("../../Design/statusbar_FM.png"), timeout =6,threshold = 0.88)
assert_exists(Template("../../Design/Radio_Local_Card.png"), timeout =6,threshold = 0.88)
assert_exists(Template("../../Design/Home_Radio_playing.png"), timeout =6,threshold = 0.88)
