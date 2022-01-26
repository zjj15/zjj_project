from autost.api import *

touch_if(Template('../../Design/OnlineVideo_Agreement_Confirm.png'), timeout=3)
touch_if(Template("../../Design/OnlineVideo_Login_cancel.png"), timeout=1)
touch_if(Template('../../Design/OnlineVideo_PlayScreen_return.png'), timeout=3)
touch_if(Template('../../Design/OnlineVideo_PlayScreen_return.png'), timeout=3)
touch(Template('../../Design/OnlineVideo_Screen_Srch.png'))

touch(Template('../../Design/OnlineVideo_InputBox_Srch.png'))

touch(Template('../../Design/OnlineVideo_SrchKeyboard_b.png'),threshold =0.8)
touch(Template('../../Design/OnlineVideo_SrchKeyboard_e.png'),threshold =0.8)
touch(Template('../../Design/OnlineVideo_SrchKeyboard_n.png'),threshold =0.8)
touch(Template('../../Design/OnlineVideo_SrchKeyboard_p.png'),threshold =0.8)
touch(Template('../../Design/OnlineVideo_SrchKeyboard_a.png'),threshold =0.8)
touch(Template('../../Design/OnlineVideo_SrchKeyboard_o.png'),threshold =0.8)

for i in range(2):
    touch(Template('../../Design/OnlineVideo_SrchKeyboard_confirm.png'),threshold =0.8)

touch(Template('../../Design/OnlineVideo_vip_icon.png'),threshold =0.8)

try:
    wait_for_appearance(Template('../../Design/OnlineVideo_Play_Bar.png'), timeout=30)
except:
    error('OnlineVideo Play VIP video Error!')

sleep(360)
