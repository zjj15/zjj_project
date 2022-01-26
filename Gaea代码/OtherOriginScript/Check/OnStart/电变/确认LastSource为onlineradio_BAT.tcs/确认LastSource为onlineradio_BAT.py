from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print('__脚本名称: ' + __file__)

do_segment(Segment('../../../../Common/BackHomeView.tcs'))
try:
    assert_exists(Template('../../../../Design/statusbar_ximalaya.png'), orv=Template('../../../../Design/statusbar_nissanradio.png'), timeout=30)
    rect_target_area=poco('android.widget.ImageView', nearest=({'text':'电台'})).get_attr('rect')
    x, y, w, h = rect_target_area
    print(rect_target_area)
    assert_not_exists(Template('../../../../Design/RadioCard_playing.png'), predict_area=[y,y+h,x,x+w])
    assert_not_exists(Template('../../../../Design/RadioCard_next.png'),  predict_area=[y,y+h,x,x+w])
    assert_not_exists(Template('../../../../Design/RadioCard_previous.png'),  predict_area=[y,y+h,x,x+w])
except:
    error('__脚本名称: ' + __file__+ 'Check error')
