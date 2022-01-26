from autost.api import *
#恢复系统设置
do_segment(Segment('../18_BackupData/I_Init_Setting_zation.tcs'))

do_segment(Segment('../../Common/BackHomeView.tcs'))

flick_to(Template('../../Design/Video_Picture_Card.png'), [970, 367], DIR_LEFT, step=1, speed=SPEED_NORMAL)
touch(Template('../../Design/Video_Picture_Card.png'), timeout=5)
sleep(5)
if poco('允许', text='允许', timeout=1).exists():
    for _ in range(3):
        if poco('允许', text='允许', timeout=1).exists():
            poco('允许', text='允许').click()
            sleep(0.5)
assert_exists(Template('../../Design/OnlineVideo_Agreement_Check.png'), timeout=10, threshold=0.95)


