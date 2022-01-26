from autost.api import *

if exists(Template("../../Design/OnlineVideo_Play_Bar.png"), timeout=3):
    touch(Template("../../Design/OnlineVideo_Playing_icon.png"), timeout=3)

assert_exists(Template("../../Design/OnlineVideo_暂停状态.png"),threshold = 0.95)
