from autost.api import *

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

touch(Template('../../Design/OnlineVideo_Next.png'),timeout=5)
assert_exists(Template('../../Design/OnlineVideo_Play_Bar.png'), timeout=35)



