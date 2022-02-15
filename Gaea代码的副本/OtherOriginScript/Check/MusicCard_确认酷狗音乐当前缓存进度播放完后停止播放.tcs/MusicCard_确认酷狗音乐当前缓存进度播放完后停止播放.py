from autost.api import *
print("__脚本名称: " + __file__)

do_segment(Segment('../../Common/BackHomeView.tcs'))

try:
    assert_exists(Template('../../Design/statusbar_kugou.png'))
    rect_target_area=poco('android.widget.ImageView', nearest=({'text':'音乐'})).get_attr('rect')
    x, y, w, h = rect_target_area
    print(rect_target_area)
    cur_song_name = poco(className='android.widget.TextView', pos2=[540, 406] ).get_attr('text')
    assert_exists(Template("../../Design/Home_Music_Closed.png"),  predict_area=[y,y+h,x,x+w], timeout=300)
except:
    error(__file__+' Error!')
