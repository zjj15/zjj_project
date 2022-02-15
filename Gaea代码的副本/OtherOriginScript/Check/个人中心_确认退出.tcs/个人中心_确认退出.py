from autost.api import *

do_segment(Segment('../../Common/BackHomeView.tcs'))

flick_to(Template('../../Design/个人中心_Card.png'), [971, 353], DIR_LEFT, step=1, speed=SPEED_NORMAL, threshold=0.95)

touch(Template('../../Design/个人中心_Card.png'), threshold=0.95)

wait_for_appearance(Template('../../Design/个人中心_提示时间不一致MSG.png'), timeout=5, threshold=0.95)
wait_for_disappearance(Template('../../Design/个人中心_提示时间不一致MSG.png'), timeout=5, threshold=0.95)

assert_exists(Template('../../Design/个人中心_实名认证.png'), threshold=0.95)
touch(Template('../../Design/个人中心_实名认证_X.png'), timeout=5)