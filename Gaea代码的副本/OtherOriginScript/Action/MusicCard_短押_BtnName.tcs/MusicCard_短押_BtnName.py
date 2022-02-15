from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print("__脚本名称: " + __file__)

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
key_name = get_param('keyname')
key_name_lower = key_name.lower()

rect_target_area=poco('android.widget.ImageView', nearest=({'text':'音乐'})).get_attr('rect')
x, y, w, h = rect_target_area
print(rect_target_area)
if 'play' == key_name_lower:
    touch(Template('../../Design/MusicCard_playing.png'),  predict_area=[y,y+h,x,x+w])
elif 'pause' == key_name_lower:
    touch(Template('../../Design/Home_Music_Closed.png'), predict_area=[y,y+h,x,x+w])
elif 'next' == key_name_lower:
    touch(Template('../../Design/MusicCard_next.png'),  predict_area=[y,y+h,x,x+w])
elif 'previous' == key_name_lower:
    touch(Template('../../Design/MusicCard_previous.png'),  predict_area=[y,y+h,x,x+w])
else:
    error('invalid param')


