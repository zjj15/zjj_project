from autost.api import *

touch(Template('../../Design/BTHF_Contact_Search_Input.png'), timeout=3)
sleep(3)


touch_if(Template('../../Design/Keyboard_English_button.png'),threshold =0.8,timeout=5)
touch(Template('../../Design/Keyboard_lower_c.png'),threshold =0.8)
touch(Template('../../Design/Keyboard_lower_e.png'),threshold =0.8)
touch(Template('../../Design/Keyboard_lower_s.png'),threshold =0.8)
touch(Template('../../Design/Keyboard_lower_h.png'),threshold =0.8)
touch(Template('../../Design/Keyboard_lower_i.png'),threshold =0.8)
touch(Template('../../Design/Keyboard_Chinese_ceshi.png'),threshold =0.8)

touch_if(Template('../../Design/Keyboard_Chinese_button.png'),threshold =0.8,timeout=5)
touch_if(Template('../../Design/Keyboard_upper_alpha.png'),threshold =0.8,timeout=5)
touch(Template('../../Design/Keyboard_upper_T.png'),threshold =0.8)

touch_if(Template('../../Design/Keyboard_lower_alpha.png'),threshold =0.8,timeout=5)
touch(Template('../../Design/Keyboard_lower_e.png'),threshold =0.8)
touch(Template('../../Design/Keyboard_lower_s.png'),threshold =0.8)
touch(Template('../../Design/Keyboard_lower_t.png'),threshold =0.8)

touch_if(Template('../../Design/Keyboard_num_button.png'),threshold =0.8,timeout=5)
touch(Template('../../Design/Keyboard_num_1.png'),threshold =0.8)

#for i in range(1):
#    touch(Template('../../Design/OnlineVideo_SrchKeyboard_confirm.png'),threshold =0.8)
