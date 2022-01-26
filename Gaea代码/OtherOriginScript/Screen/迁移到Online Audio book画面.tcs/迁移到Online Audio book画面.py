from autost.api import *
DEV1 = ST.DEV1

do_segment(Segment('../../Common/BackHomeView.tcs'))

flick_to(Template('../../Design/Radio_Card.png'), [1788, 332], DIR_LEFT, device=DEV1)

touch(Template('../../Design/Radio_Card.png'), device=DEV1)

poco('懒人听书', text='懒人听书', timeout=4).click()

if poco(text='不再提醒', timeout=3.0).exists():
    poco('bubei.tingshu.hd.nissan:id/checkBox').click()
    poco(text='同意并继续').click()

sleep(2)

try:
    assert_exists(Template('../../Design/Radio_Ianren_button_focus.png'), device=DEV1)

except:
    error('IntoIanrenRadio Error!')

