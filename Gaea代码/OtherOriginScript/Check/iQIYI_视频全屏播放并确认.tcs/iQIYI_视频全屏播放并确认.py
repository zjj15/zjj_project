from autost.api import *

touch_if(Template("../../Design/OnlineVideo_Login_cancel.png"), timeout=1)

assert_exists(Template("../../Design/OnlineVideo_Play_Bar.png"), timeout=30)

touch([972, 377])
assert_not_exists(Template("../../Design/OnlineVideo_Play_Bar.png"), timeout=5)
#退出全屏
touch([972, 377])