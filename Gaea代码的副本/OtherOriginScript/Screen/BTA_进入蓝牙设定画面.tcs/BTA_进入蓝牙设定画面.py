from autost.api import *
#当前画面是BT Audio画面
if exists(Template("../../Design/SettingBar_bt_focus.png"), timeout=3):
    pass
else:
    touch([248, 161])

    flick_to(Template("../../Design/SettingBar_bt_nofocus.png"), [303, 373], DIR_DOWN, step=1, speed=SPEED_NORMAL)

    touch_if(Template("../../Design/SettingBar_bt_nofocus.png"), timeout=3)

try:
    assert_exists(Template("../../Design/SettingBar_bt_focus.png"))
    assert_exists(Template("../../Design/Setting_BT.png"))
except:
    error('IntoBTSetting Error!')
