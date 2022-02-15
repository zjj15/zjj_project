from autost.api import *

do_segment(Segment('../../Common/BackHomeView.tcs'))

flick_to(Template('../../Design/Music_Card.png'), [971, 353], DIR_LEFT, step=1, speed=SPEED_NORMAL)

touch(Template('../../Design/Music_Card.png'))

poco('酷狗音乐', text='酷狗音乐', timeout=4).click()
if poco('不再提醒', text='不再提醒', timeout=5).exists():
    poco('不再提醒', text='不再提醒').click()
if poco('同意并继续', text='同意并继续', timeout=5).exists():
    poco('同意并继续', text='同意并继续', timeout=4).click()
if poco('去授权', text='去授权', timeout=2).exists():
    poco('去授权', text='去授权').click()
for _ in range(2):
    if poco('允许', text='允许', timeout=4).exists():
        poco('允许', text='允许').click()
    else:
        break
try:
    assert_exists(Template('../../Design/ShortBar_KuGou_focus.png'))
    assert_exists(Template('../../Design/KuGou_Source.png'))
except:
    error('IntoKuGou Error!')
