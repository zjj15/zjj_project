from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

do_segment(Segment('../Navi_进入检索画面.tcs'))


touch_if(Template('../../Design/Navi_input_switch_button.png'),threshold =0.8,timeout=5)
touch_if(Template('../../Design/Navi_input_pinyin.png'),threshold =0.8,timeout=5)
if exists(Template('../../Design/Navi_search_history_rmgc.png'), timeout=2, threshold=0.94):
    touch(Template('../../Design/Navi_search_history_rmgc.png'), threshold=0.94)
else:
    touch(Template('../../Design/Navi_Keyboard_lower_r.png'),threshold =0.8)    
    touch(Template('../../Design/Navi_搜索_Keyboard_m.png'), threshold=0.94)
    touch(Template('../../Design/Navi_Keyboard_lower_g.png'),threshold =0.8)    
    touch(Template('../../Design/Navi_Keyboard_lower_c.png'),threshold =0.8)    
    touch(Template('../../Design/input_search_rmgc.png'), threshold=0.94)
    sleep(5)
    touch_if(Template('../../Design/Navi_search_result_rmgc.png'), threshold=0.94)
    sleep(3)