from autost.api import *

try:
    if exists(Template('../../../Design/Home_Page1_order.png'),threshold = 0.9,timeout=5) or exists(Template('../../../Design/Home_Page1_order_1.png'),threshold = 0.9,timeout=5):
        pass
    else:
        error('Home Card page 1 order Error!')
 
    flick_to(Template('../../../Design/Home_Page2_bar.png'), [960, 386], DIR_LEFT, step=1, speed=SPEED_NORMAL)
 
    assert_exists(Template('../../../Design/Home_Page2_order.png'),threshold = 0.9)
 
    flick_to(Template('../../../Design/Home_Page3_bar.png'), [953, 364], DIR_LEFT, step=1, speed=SPEED_NORMAL)
 
    assert_exists(Template('../../../Design/Home_Page3_order.png'),threshold = 0.9)
except:
    error('Home Card order Error!')