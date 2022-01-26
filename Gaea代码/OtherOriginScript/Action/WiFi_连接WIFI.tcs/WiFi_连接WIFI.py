from autost.api import *

print("__脚本名称: " + __file__)

touch_if(Template('../../Design/WIFI_ignore_icon.png'), timeout=3, threshold=0.95)
if exists(Template('../../Design/wifi_setting_signal_4.png'), timeout=3, threshold=0.95):
    touch(Template('../../Design/wifi_setting_signal_4.png'), timeout=3, threshold=0.95)
elif exists(Template('../../Design/wifi_setting_signal_3.png'), timeout=3, threshold=0.95):
    touch(Template('../../Design/wifi_setting_signal_3.png'), timeout=3, threshold=0.95)
