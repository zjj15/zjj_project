from autost.api import * 

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print('__脚本名称: ' + __file__)


i = 0
while exists(Template('../../Design/Navi_menu_back.png'), timeout=3, threshold=0.93, device=DEV1):
    if i>10:
        break
    touch_if(Template('../../Design/Navi_menu_back.png'), timeout=3, threshold=0.93, device=DEV1)
    i+=1
if not exists(Template("../../Design/Navi_target.png"), threshold=0.90, device=DEV1):
    do_segment(Segment("../../Action/NAVI_结束模拟导航.tcs"))
    sleep(5)

assert_exists(Template('../../Design/Navi_mine_button.png'))
