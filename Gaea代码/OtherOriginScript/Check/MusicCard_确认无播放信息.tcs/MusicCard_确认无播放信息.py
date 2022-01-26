from autost.api import *
DEV1="Gaea://127.0.0.1:5037/GFEDCBA0987654321"

do_segment(Segment('../../Common/BackHomeView.tcs'))

assert_exists(Template('../../Design/Music_Card_NotStarted.png'), threshold=0.90)



