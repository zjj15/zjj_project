from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
# 设定热点为ON
do_segment(Segment('../../../Action/设定热点为ON.tcs'))
try:
    assert_exists(Template('../../../Design/hotpoint_changed_password_icon.png'),device=DEV1)
except:
    error('check hotpoint password fail!') 