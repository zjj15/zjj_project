from autost.api import *
DEV1 = ST.DEV1
#同意并继续
do_segment(Segment('../../Common/BackHomeView.tcs'))

flick_to(Template('../../Design/Radio_Card.png'), [1788, 332], DIR_LEFT, device=DEV1)

touch(Template('../../Design/Radio_Card.png'), device=DEV1)

poco('懒人听书', text='懒人听书', timeout=4).click()
if poco('不再提醒', text='不再提醒', timeout=2).exists():
    poco('不再提醒', text='不再提醒').click()
if poco('同意并继续', text='同意并继续', timeout=2).exists():
    poco(text='同意并继续').click()
for _ in range(2):
    if poco('允许', text='允许', timeout=4).exists():
        poco('允许', text='允许').click()
try:
    assert_exists(Template('../../Design/AudioBooks_Local_button_focus.png'), device=DEV1)
except:
    error('IntoLocalAudioBooks Error!')
