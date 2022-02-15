from autost.api import *

touch_if(Template('../../../Design/OnlineVideo_Agreement_Confirm.png'), timeout=2)

touch_if(Template('../../../Design/OnlineVideo_return_icon.png'), timeout=2)
touch_if(Template("../../../Design/OnlineVideo_Center.png"), timeout=2, threshold=0.93)
touch_if(Template('../../../Design/OnlieVideo_Setting_View_History.png'), timeout=2)

try:
    assert_exists(Template(os.path.join(ST.LOG_DIR, ST.OnlineVideo_View_History)))
except:
    error('OnlineVideo View History Check K Error!')

