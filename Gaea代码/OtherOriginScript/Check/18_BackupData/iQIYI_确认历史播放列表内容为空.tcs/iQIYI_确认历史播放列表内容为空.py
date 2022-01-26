from autost.api import *

touch_if(Template('../../../Design/OnlineVideo_Agreement_Confirm.png'), timeout=2)

touch_if(Template('../../../Design/OnlineVideo_return_icon.png'), timeout=2)
touch_if(Template('../../../Design/OnlineVideo_Center.png'), timeout=2, threshold=0.93)

touch_if(Template('../../../Design/OnlieVideo_Setting_View_History.png'), timeout=2)

assert_exists(Template('../../../Design/OnlieVideo_暂无观看历史.png'), timeout=2, threshold=0.93)


