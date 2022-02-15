from autost.api import *

if exists(Template("../../Design/OnlineVideo_Playing_icon.png"),threshold = 0.95, timeout = 2):
    touch(Template("../../Design/OnlineVideo_Playing_icon.png"),threshold = 0.95, timeout = 2)
    assert_exists(Template("../../Design/OnlineVideo_暂停btn.png"),threshold = 0.95, timeout = 5)
elif exists(Template("../../Design/OnlineVideo_暂停btn.png"),threshold = 0.95, timeout = 2):
    touch(Template("../../Design/OnlineVideo_暂停btn.png"),threshold = 0.95, timeout = 2)
    assert_exists(Template("../../Design/OnlineVideo_Playing_icon.png"),threshold = 0.95, timeout = 5)
else:
    error("iQIYI 非播放中状态！！！")