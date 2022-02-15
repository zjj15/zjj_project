from autost.api import *


do_segment(Segment('../../Screen/迁移到中控设定画面.tcs'))
do_segment(Segment('../../Screen/进入蓝牙设定画面.tcs'))
#if poco('配对列表', text='配对列表', timeout=1).exists():
for _ in range(8):
    if not poco('配对列表', text='配对列表', timeout=1).exists():
        break
    if poco('断开', text='断开', timeout=1).exists():
        poco('断开', text='断开').click()
        sleep(5)
    if exists(Template("../../Design/bt_setting_btn_删除.png"), timeout=1):
        touch(Template("../../Design/bt_setting_btn_删除.png"), timeout=2)
else:
    error(__file__+' error')
    
    
    