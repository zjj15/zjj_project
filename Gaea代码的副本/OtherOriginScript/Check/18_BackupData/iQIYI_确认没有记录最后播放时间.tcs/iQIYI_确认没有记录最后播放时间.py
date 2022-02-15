from autost.api import *

touch_if(Template('../../../Design/OnlineVideo_Agreement_Confirm.png'), timeout=2)

touch_if(Template("../../../Design/OnlineVideo_Center.png"), timeout=2, threshold=0.93)

touch_if(Template('../../../Design/OnlieVideo_Setting_View_History.png'), timeout=2)

try:
    assert_exists(Template('../../../Design/OnlineVideo_RecentView_empty.png'))
except:
    error('Onlien Video Recent View empty Chcek Error!')
