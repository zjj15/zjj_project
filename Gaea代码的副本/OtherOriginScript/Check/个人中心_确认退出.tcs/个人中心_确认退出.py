from autost.api import *

do_segment(Segment('../../Common/BackHomeView.tcs'))

flick_to(Template('../../Design/��������_Card.png'), [971, 353], DIR_LEFT, step=1, speed=SPEED_NORMAL, threshold=0.95)

touch(Template('../../Design/��������_Card.png'), threshold=0.95)

wait_for_appearance(Template('../../Design/��������_��ʾʱ�䲻һ��MSG.png'), timeout=5, threshold=0.95)
wait_for_disappearance(Template('../../Design/��������_��ʾʱ�䲻һ��MSG.png'), timeout=5, threshold=0.95)

assert_exists(Template('../../Design/��������_ʵ����֤.png'), threshold=0.95)
touch(Template('../../Design/��������_ʵ����֤_X.png'), timeout=5)