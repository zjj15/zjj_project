from autost.api import *

touch_if(Template('../../Design/OnlineVideo_Agreement_Confirm.png'), timeout=3)
touch_if(Template("../../Design/OnlineVideo_Login_cancel.png"), timeout=1)
do_segment(Segment('../../Action/iQIYI_选择tab_tabname.tcs'), tabname='VIP专区')
for i in range(3):
    touch_if(Template('../../Design/OnlineVideo_VIP_Bar.png'), timeout=5)
    if exists(Template('../../Design/OnlineVideo_VIP_Bar_focus.png'), timeout=2):
        break

 


