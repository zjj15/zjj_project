from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print('__脚本名称: ' + __file__)

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

keyevent(ITCMD_MENU)
keyevent(ITCMD_MENU)

poco('电台', text='电台').assert_exists()

cur_program_name = ''
if poco(className='android.widget.TextView', pos2=[994, 406] ).exists():
    cur_program_name = poco(className='android.widget.TextView', pos2=[994, 406] ).get_attr('text')
print('当前播放的内容是：'+cur_program_name)
rect_target_area = poco('android.widget.ImageView', pos2=[1146, 536]).get_attr('rect')
x, y, w, h = rect_target_area
try:
    if 'FM' in cur_program_name:
        pass
    elif exists(Template('../../Design/Home_Radio_playing.png'),  predict_area=[y,y+h,x,x+w], timeout=1):
        # 式样变更：nissan radio-> ximalaya
        assert_not_exists(Template('../../Design/statusbar_ximalaya.png'), threshold=0.95)
        #assert_not_exists(Template('../../Design/statusbar_nissanradio.png'), threshold=0.95)
    else:
        assert_exists(Template('../../Design/Home_Radio_Closed.png'),  predict_area=[y,y+h,x,x+w])
except:
    error('当前播放的内容有：'+cur_program_name)
