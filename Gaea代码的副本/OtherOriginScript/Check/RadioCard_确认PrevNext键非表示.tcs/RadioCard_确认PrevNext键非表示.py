from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print('__脚本名称: ' + __file__)

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

keyevent(ITCMD_MENU)
keyevent(ITCMD_MENU)

poco('电台', text='电台').assert_exists()

try:
    rect_target_area=poco('android.widget.ImageView', nearest=({'text':'电台'})).get_attr('rect')
    x, y, w, h = rect_target_area
    print(rect_target_area)
    assert_exists(Template('../../Design/Home_Radio_Closed.png'), predict_area=[y,y+h,x,x+w])
    assert_not_exists(Template('../../Design/RadioCard_next.png'),  predict_area=[y,y+h,x,x+w])
    assert_not_exists(Template('../../Design/RadioCard_previous.png'),  predict_area=[y,y+h,x,x+w])
finally:
    ST.OnlineMusic_song_name = None
