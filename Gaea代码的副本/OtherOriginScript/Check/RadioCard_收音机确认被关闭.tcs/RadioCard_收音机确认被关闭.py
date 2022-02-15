from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print('__脚本名称: ' + __file__)

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

keyevent(ITCMD_MENU)
keyevent(ITCMD_MENU)

poco('电台', text='电台').assert_exists()

cur_program_name = poco(className='android.widget.TextView', pos2=[994, 406] ).get_attr('text')
rect_target_area = poco('android.widget.ImageView', pos2=[1146, 536]).get_attr('rect')
x, y, w, h = rect_target_area

if 'FM' in cur_program_name:
    assert_exists(Template('../../Design/Home_Radio_Closed.png'), predict_area=[y,y+h,x,x+w])
else:
    error('cur_program_name：' + cur_program_name)
