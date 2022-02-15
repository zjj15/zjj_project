from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
DEV2 = 'GAEA_Camera:///'
print('__脚本名称: ' + __file__)

if exists(Template('../../Design/Manual_Card.png'), timeout=3):
    pass
else:
    do_segment(Segment('../../Common/BackHomeView.tcs'))

    flick_to(Template('../../Design/More_Card.png'), [957, 347], DIR_LEFT, step=1, speed=SPEED_NORMAL)

    touch(Template('../../Design/More_Card.png'))
touch(Template('../../Design/Manual_Card.png'))
