from autost.api import *
## fix:wifi signl bad
for _ in range(20):
    if exists(Template('pic/capture_20210715134359601287.png'), timeout=1):
        sleep(2)
    else:
        break
else:
    error('wifi signl bad:iQIYI_关闭自动跳过片头片尾btn showing...')

if exists(Template('../../Design/SkipHeaderTailer_ON.png'), timeout=2, threshold=0.88):
    touch_in(Template('../../Design/OnlineVideo_BitStreamQualit_On_icon.png'),Template('../../Design/SkipHeaderTailer_ON.png'), timeout=2, threshold=0.88)
try:
    assert_exists(Template('../../Design/SkipHeaderTailer_OFF.png'), timeout=5)
except:
    error('SkipHeaderTailer Switch ON Error!')
