from autost.api import *
DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

do_segment(Segment('../../Common/BackHomeView.tcs'))

flick_to(Template('../../Design/InCarKTV_Card.png'), [968, 342], DIR_LEFT, step=1, speed=SPEED_NORMAL)
sleep(1.5)
touch(Template('../../Design/InCarKTV_Card.png'))
for _ in range(100):
    if poco('com.changba.sd:id/iv_slogen', timeout=3).exists() or poco('com.changba.sd:id/iv_logo', timeout=3).exists():
        sleep(1)
    else:
        break
for _ in range(4):
    if poco('允许', text='允许', timeout=1).exists():
        poco('允许', text='允许').click()
touch_if(Template('../../Design/InCarKTV_checkbox.png'), timeout=3)
touch_if(Template('../../Design/InCarKTV_agree.png'), timeout=3)
try:
    #assert_exists(Template('../../Design/InCarKTV_ShortBar.png'))
    assert_exists(Template('../../Design/InCarKTV_Source.png'))
except:
    error('IntoInCarKTV Error!')




