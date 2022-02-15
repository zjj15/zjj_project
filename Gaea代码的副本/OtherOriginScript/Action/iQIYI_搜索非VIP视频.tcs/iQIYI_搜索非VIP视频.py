from autost.api import *

touch_if(Template('../../Design/OnlineVideo_Agreement_Confirm.png'), timeout=3)
touch_if(Template("../../Design/OnlineVideo_Login_cancel.png"), timeout=1)
do_segment(Segment('../iQIYI_选择tab_tabname.tcs'), tabname='电视剧')

if exists(Template('../../Design/OnlineVideo_筛选中.png'), timeout=3,threshold =0.95):
    touch(Template('../../Design/OnlineVideo_筛选中.png'), timeout=3,threshold =0.95)
touch(Template('../../Design/OnlineVideo_筛选.png'), timeout=3,threshold =0.95)

flick_to(Template('../../Design/OnlineVideo_筛选_免费.png'), [612, 392], DIR_LEFT)
touch(Template('../../Design/OnlineVideo_筛选_免费.png'), timeout=3,threshold =0.96)
sleep(5)
