from autost.api import *

do_segment(Segment('../../../Screen/迁移到中控设定画面.tcs'))

if exists(Template('../../../Design/SettingBar_Other_focus.png'), timeout=2):
    pass
else:
    touch([248, 161])
 
    flick_to(Template('../../../Design/SettingBar_Other_nofocus.png'), [290, 485], DIR_UP, step=1, speed=SPEED_NORMAL)
 
    touch(Template('../../../Design/SettingBar_Other_nofocus.png'))
 
flick_to(Template('../../../Design/Setting_Factory_Reset.png'), [900, 657], DIR_UP, step=1, speed=SPEED_NORMAL)

touch(Template('../../../Design/Setting_Factory_Reset.png'))

touch(Template('../../../Design/FactoryReset_Confirm.png'))
 
try:
    assert_exists(Template('../../../Design/FactoryReset_Success.png'))
except:
    error('Setting Initialization Error!')


do_segment(Segment('../../../../InfraLib/Screens/Setting/App权限列表画面/scripts/打开个人中心全部权限.tcs'))
do_segment(Segment('../../../../InfraLib/Screens/Setting/App权限列表画面/scripts/打开酷狗音乐全部权限.tcs'))
do_segment(Segment('../../../../InfraLib/Screens/Setting/App权限列表画面/scripts/打开输入法全部权限.tcs'))
do_segment(Segment('../../../../InfraLib/Screens/Setting/App权限列表画面/scripts/打开在线视频全部权限.tcs'))
do_segment(Segment('../../../../InfraLib/Screens/Setting/App权限列表画面/scripts/打开喜马拉雅全部权限.tcs'))
do_segment(Segment('../../../../InfraLib/Screens/Setting/App权限列表画面/scripts/打开懒人听书全部权限.tcs'))
