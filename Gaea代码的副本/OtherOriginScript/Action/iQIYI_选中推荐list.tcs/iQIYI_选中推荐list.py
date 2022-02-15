from autost.api import *

if exists(Template("../../Design/OnlineVideo_推荐_focus.png"), timeout=2) or exists(Template("../../Design/OnlineVideo_推荐_nofocus.png"), timeout=2):
    touch_if(Template("../../Design/OnlineVideo_推荐_nofocus.png"), timeout=1)