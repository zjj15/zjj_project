from autost.api import *

if exists(Template('../../Design/OnlineVideo_推荐_focus.png'), timeout=2) or exists(Template('../../Design/OnlineVideo_推荐_nofocus.png'), timeout=2):
    touch_if(Template('../../Design/OnlineVideo_推荐_nofocus.png'), timeout=1)
    wait_for_disappearance(Template('../../Design/OnlineVideo_推荐list_空.png'))

assert_not_exists(Template(os.path.join(ST.LOG_DIR, ST.OnlineVideo_recommendation_list)))
