from autost.api import *
print("__脚本名称: " + __file__)

do_segment(Segment('../../Common/BackHomeView.tcs'))

try:
    assert_exists(Template('../../Design/statusbar_kugou.png'))
    rect_target_area=poco('android.widget.ImageView', nearest=({'text':'音乐'})).get_attr('rect')
    x, y, w, h = rect_target_area
    print(rect_target_area)
    assert_exists(Template('../../Design/MusicCard_next.png'),  predict_area=[y,y+h,x,x+w])
    assert_exists(Template('../../Design/MusicCard_playing.png'),  predict_area=[y,y+h,x,x+w])
    assert_exists(Template('../../Design/MusicCard_previous.png'),  predict_area=[y,y+h,x,x+w])

except:
    error('AudioBook Card Check Error!')
