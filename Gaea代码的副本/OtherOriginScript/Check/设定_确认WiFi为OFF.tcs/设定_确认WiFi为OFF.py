from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

try:
    assert_exists(Template('../../Design/wifi_setting_off_icon.png'),device=DEV1)

except:
    error('check wifi off fail!') 

#后置条件
##打开wifi
sleep(2)
#do_segment(Segment('../../Action/WiFi 设定为ON.tcs'))

