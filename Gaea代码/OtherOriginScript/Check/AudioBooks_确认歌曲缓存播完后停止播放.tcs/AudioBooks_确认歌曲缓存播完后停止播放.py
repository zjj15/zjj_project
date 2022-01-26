from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
#flick_to(Template('../../Design/Radio_Card.png'), [1788, 332], DIR_LEFT, device=DEV1)


if poco('android.widget.ImageView', pos=(0.61875, 0.37569444444444444)).exists():
    poco('android.widget.ImageView', pos=(0.61875, 0.37569444444444444)).click()
if poco('bubei.tingshu.hd.nissan:id/iv_pause_play').exists():
    pass

#wait_for_appearance(Template('../../Design/AudioBooks_card_stop_icon.png'), timeout=200)
