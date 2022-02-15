from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print('__脚本名称: ' + __file__)

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

keyevent(ITCMD_MENU)
keyevent(ITCMD_MENU)

poco('电台', text='电台').assert_exists()

rect_target_area = poco('android.widget.ImageView', pos2=[992, 112]).get_attr('rect')
x, y, w, h = rect_target_area
try:
    if exists(Template('../../Design/Home_Radio_playing.png'),  predict_area=[y,y+h,x,x+w], timeout=2):
        assert_not_exists(Template('../../Design/statusbar_audiobooks.png'))
    else:
        assert_exists(Template('../../Design/Home_Radio_Closed.png'),  predict_area=[y,y+h,x,x+w])
finally:
    pass
