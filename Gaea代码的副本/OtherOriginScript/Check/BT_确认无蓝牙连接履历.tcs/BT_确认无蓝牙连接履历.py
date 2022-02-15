from autost.api import * 

print('__脚本名称: ' + __file__)

do_segment(Segment("../../Screen/迁移到中控设定画面.tcs"))
do_segment(Segment("../../Screen/进入蓝牙设定画面.tcs"))
poco('配对列表', text='配对列表').assert_not_exists()
