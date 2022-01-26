from autost.api import *

if exists(Template("../../Design/OnlineVideo_清晰度框.png"), timeout=2, threshold=0.96):
    touch(Template("../../Design/OnlineVideo_清晰度框.png"), timeout=1, threshold=0.96)
else:
    touch([327, 644])

if poco('1080P', text='1080P', timeout=2).exists():
    error("iQIYI_确认不能选择1080p check:error!!!")

touch([327, 644])
