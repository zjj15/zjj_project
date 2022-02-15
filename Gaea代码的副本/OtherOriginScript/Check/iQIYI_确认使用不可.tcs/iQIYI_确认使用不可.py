from autost.api import *

assert_not_exists(Template("../../Design/ShortBar_OnlineVideo_focus.png"), timeout=10, threshold = 0.95)
assert_not_exists(Template("../../Design/OnlineVideo_Center.png"), timeout=5)
