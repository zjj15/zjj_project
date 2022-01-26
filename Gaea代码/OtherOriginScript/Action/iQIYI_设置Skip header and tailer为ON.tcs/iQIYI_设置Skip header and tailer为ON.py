from autost.api import *

touch_if(Template('../../Design/OnlineVideo_Login_cancel.png'), timeout=1)
for _ in range(20):
    if exists(Template('../../Design/SkipHeaderTailer_ON.png'), timeout=1, threshold=0.88):
        break
    if exists(Template('../../Design/SkipHeaderTailer_OFF.png'), timeout=1):
        touch_in(Template('../../Design/SkipHeaderTailer_OFF_Switch.png'), Template('../../Design/SkipHeaderTailer_OFF.png'), timeout=3)
else:
    error('SkipHeaderTailer Switch ON Error!')
