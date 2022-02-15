from autost.api import *
#脚本图片有问题，待修正
do_segment(Segment('../../Common/BackHomeView.tcs'))

try:
    assert_exists(Template('../../Design/Radio_AudioBook_Card.png'))
except:
    error('AudioBook Card Check Error!')
'''
from autost.api import *
print("__脚本名称: " + __file__)

do_segment(Segment('../../Common/BackHomeView.tcs'))

try:
    assert_exists(Template('../../Design/statusbar_audiobooks.png'))
    rect_target_area=poco('android.widget.ImageView', nearest=({'text':'电台'})).get_attr('rect')
    x, y, w, h = rect_target_area
    print(rect_target_area)
    assert_exists(Template('../../Design/RadioCard_next.png'),  predict_area=[y,y+h,x,x+w])
    assert_exists(Template('../../Design/RadioCard_playing.png'),  predict_area=[y,y+h,x,x+w])
    assert_exists(Template('../../Design/RadioCard_previous.png'),  predict_area=[y,y+h,x,x+w])

except:
    error(__file__+' Check Error!')
'''
