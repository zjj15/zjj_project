from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
## case：车机重启后，bt已连接ons弹出，touch失败
for _ in range(3):
    if exists(Template('../../Design/wifi_setting_on_icon.png'), timeout=3,device=DEV1):
        touch_in(Template('../../Design/setting_on_icon.png'),Template('../../Design/wifi_setting_on_icon.png'), device=DEV1)
    if exists(Template('../../Design/wifi_setting_off_icon.png'), timeout=1.5, device=DEV1):
        break
try:
    assert_exists(Template('../../Design/wifi_setting_off_icon.png'),device=DEV1)
except:
    error('set wifi off fail!') 


if exists(Template('../../Design/hot_point_off_icon.png'), timeout=3,device=DEV1):
    touch_in(Template('../../Design/setting_off_icon.png'),Template('../../Design/hot_point_off_icon.png'), device=DEV1)

try:
    if exists(Template('../../Design/hotpoit_password_icon.png'), timeout=3,device=DEV1):
        pass
    else:
        poco('“车辆热点”密码', text='“车辆热点”密码').assert_exists()
except:
    error('open hotpoint fail!') 

