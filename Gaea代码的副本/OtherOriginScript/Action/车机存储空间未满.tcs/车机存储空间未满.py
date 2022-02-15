from autost.api import *

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

do_segment(Segment('../../Screen/进入其他设定画面.tcs'))

swipe([1087, 667], [1087, 220], step=15, speed=SPEED_NORMAL)
swipe([1087, 667], [1087, 220], step=15, speed=SPEED_NORMAL)


assert_exists(Template('../../Design/user_space_not_full_icon.png'),threshold=0.8)