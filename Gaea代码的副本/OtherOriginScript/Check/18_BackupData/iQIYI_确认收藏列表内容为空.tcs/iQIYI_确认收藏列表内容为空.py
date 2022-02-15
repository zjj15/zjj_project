from autost.api import *

touch_if(Template("../../../Design/OnlineVideo_Center.png"), timeout=2, threshold=0.93)

touch_if(Template('../../../Design/onlinevideo_my_favorite_not_select_icon.png'), timeout=2)

try:
    assert_not_exists(Template(os.path.join(ST.LOG_DIR, ST.OnlineVideo_favourite)))
except:
    error('OnlineVideo Favourite Check I Error!')
