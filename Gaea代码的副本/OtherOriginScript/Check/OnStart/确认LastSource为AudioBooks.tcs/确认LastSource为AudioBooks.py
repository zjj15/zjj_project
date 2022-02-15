from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print('__脚本名称: ' + __file__)

for i in range(3):
    if (not exists(Template('../../../Design/Home_mark_focus.png'), timeout=2,threshold=0.90, device=DEV1) and not exists(Template('../../../Design/Home_mark_nofocus.png'), timeout=2,threshold=0.90, device=DEV1)):
        wait_for_appearance(Template('../../../Design/Home_Page1_Bar.png'), timeout=60, device=DEV1)
    else:
        pass
    do_segment(Segment('../../../Common/BackHomeView.tcs'))
    sleep(2)


try:
    assert_exists(Template('../../../Design/statusbar_audiobooks.png'), orv=Template('../../../Design/statusbar_ximalaya.png'),threshold=0.90, device=DEV1)
    rect_target_area=poco('android.widget.ImageView', nearest=({'text':'电台'})).get_attr('rect')
    x, y, w, h = rect_target_area
    print(rect_target_area)
#    no display icon exists when accoffon\boffon\mmioffon
##    assert_exists(Template('../../../Design/RadioCard_playing.png'), predict_area=[y,y+h,x,x+w])
    assert_exists(Template('../../../Design/RadioCard_next.png'),  predict_area=[y,y+h,x,x+w])
    assert_exists(Template('../../../Design/RadioCard_previous.png'),  predict_area=[y,y+h,x,x+w])
except:
    error('__脚本名称: ' + __file__+ 'Check error')
