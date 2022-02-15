from autost.api import *
DEV1 = ST.DEV1
if exists(Template('../../Design/Radio_Local_button_focus.png'), device=DEV1, timeout = 1):
    pass
elif exists(Template('../../Design/Radio_Local_button.png'), device=DEV1, timeout = 1):
    touch(Template('../../Design/Radio_Local_button.png'), device=DEV1, timeout = 1)
else:
    do_segment(Segment('../../Common/BackHomeView.tcs'))
    flick_to(Template('../../Design/Radio_Card.png'), [1788, 332], DIR_LEFT, device=DEV1)
    for i in range(3):
        touch_if(Template('../../Design/Radio_Card.png'), device=DEV1, timeout = 1)
        touch_if(Template('../../Design/Radio_Local_button.png'), device=DEV1, timeout = 2,threshold=0.92)
        if exists(Template('../../Design/Radio_Local_button_focus.png'), device=DEV1, timeout = 2):
            break
try:
    assert_exists(Template('../../Design/Radio_Local_button_focus.png'), device=DEV1)
    ST.FM_Channel = 'FM_Channel.png'
    snapshot(rect=[895, 235, 249, 89], filename=os.path.join(ST.LOG_DIR, ST.FM_Channel))
except:
    error('IntoLocalRadio FM Error!')
