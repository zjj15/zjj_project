from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

do_segment(Segment('../Navi_进入检索画面.tcs'))


touch_if(Template('../../Design/Navi_input_switch_button.png'),threshold =0.8,timeout=5)
touch_if(Template('../../Design/Navi_input_pinyin.png'),threshold =0.8,timeout=5)
touch(Template('../../Design/Navi_Keyboard_lower_c.png'),threshold =0.8)
touch(Template('../../Design/Navi_Keyboard_lower_e.png'),threshold =0.8)
touch(Template('../../Design/Navi_Keyboard_lower_s.png'),threshold =0.8)
touch(Template('../../Design/Navi_Keyboard_lower_h.png'),threshold =0.8)
touch(Template('../../Design/Navi_Keyboard_lower_i.png'),threshold =0.8)
touch(Template('../../Design/Navi_Keyboard_Chinese_ceshi.png'),threshold =0.8)


touch_if(Template('../../Design/Navi_input_switch_button.png'),threshold =0.8,timeout=5)
touch_if(Template('../../Design/Navi_input_firstAlpha.png'),threshold =0.8,timeout=5)
touch(Template('../../Design/Navi_Keyboard_upper_T.png'),threshold =0.8)

touch_if(Template('../../Design/Navi_input_switch_button.png'),threshold =0.8,timeout=5)
touch_if(Template('../../Design/Navi_input_pinyin.png'),threshold =0.8,timeout=5)
touch(Template('../../Design/Navi_Keyboard_lower_e.png'),threshold =0.8)
touch(Template('../../Design/Navi_Keyboard_lower_s.png'),threshold =0.8)
touch(Template('../../Design/Navi_Keyboard_lower_t.png'),threshold =0.8)
touch_if(Template('../../Design/Navi_input_switch_button.png'),threshold =0.8,timeout=5)
touch_if(Template('../../Design/Navi_input_firstAlpha.png'),threshold =0.8,timeout=5)



touch_if(Template('../../Design/Navi_search_input_num_icon.png'),threshold =0.8,timeout=5)
touch(Template('../../Design/Navi_Keyboard_num_1.png'),threshold =0.8)


try:
    assert_exists(Template('../../Design/IME_Navi_input.png'), threshold=0.90)
except:
    error('__脚本名称: ' + __file__+ 'Check error')
