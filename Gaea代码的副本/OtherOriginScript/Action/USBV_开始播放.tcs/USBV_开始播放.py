from autost.api import *
def driving_restrictoff():
    if exists(Template('../../Design/OnlineVideo_走形规制_安全提示MSG.png'),threshold = 0.95, timeout = 1):
        do_segment(Segment('../DrivingRestrictOff.tcs'))

driving_restrictoff()
touch([607, 34])

touch_if(Template('../../Design/USBVideo_File_Button.png'), timeout=2)
driving_restrictoff()
touch([607, 34])

touch_if(Template('../../Design/USBVideo_Pause_Button.png'))

try:
    assert_exists(Template('../../Design/USBVideo_Play_Bar.png'))
except:
    error('USB Video Play Error!')

