from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

touch(Template('../../Design/hotpoit_password_icon.png'), timeout=3,device=DEV1)
sleep(1)
touch_if(Template('../../Design/input_English_g.png'), timeout=3,device=DEV1)
touch_if(Template('../../Design/input_English_a.png'), timeout=3,device=DEV1)
touch_if(Template('../../Design/input_English_e.png'), timeout=3,device=DEV1)
touch_if(Template('../../Design/input_English_a.png'), timeout=3,device=DEV1)
touch_if(Template('../../Design/input_English_g.png'), timeout=3,device=DEV1)
touch_if(Template('../../Design/input_English_a.png'), timeout=3,device=DEV1)
touch_if(Template('../../Design/input_English_e.png'), timeout=3,device=DEV1)
touch_if(Template('../../Design/input_English_a.png'), timeout=3,device=DEV1)
touch_if(Template('../../Design/input_complete_icon.png'), timeout=3,device=DEV1)


try:
    assert_exists(Template('../../Design/hotpoint_changed_password_icon.png'),device=DEV1)
except:
    error('change hotpoint password fail!')