from autost.api import * 

print('__脚本名称: ' + __file__)

#do_segment(Segment('../../Screen/迁移到中控设定画面.tcs'))
#do_segment(Segment('../../Screen/进入蓝牙设定画面.tcs'))
assert_exists(Template('../../Design/statusbar_bt_mark.png'), threshold=0.92, timeout=45)
