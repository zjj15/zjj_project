from autost.api import *
#当前画面为中控设定画面

for _ in range(2):
    touch_if(Template('../../Design/BT_setting_onfocus.png'), timeout=3)
    #poco('蓝牙', text='蓝牙', timeout=2).exists()

assert_exists(Template('../../Design/BT_setting_selected_icon.png'))