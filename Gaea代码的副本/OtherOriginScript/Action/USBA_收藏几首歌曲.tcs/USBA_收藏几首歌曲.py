from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
#前置条件
##打开USB端口
do_segment(Segment("../../Common/openUSB_all.tcs"))

for _ in range(2):
    touch(Template('../../Design/usbaudio_next_song_button.png'), device=DEV1)
    touch_if(Template('../../Design/usbaudio_not_favorite_icon.png'), timeout=3,device=DEV1)

touch(Template('../../Design/usbaudio_display_button.png'), device=DEV1)
touch_if(Template('../../Design/usbaudio_my_favorite_next_selected_icon.png'), timeout=3, device=DEV1)
sleep(2)
ST.usbaudio_favorite_list = snapshot(rect=[507, 144, 888, 426], device=DEV1)
touch(Template('../../Design/usbaudio_display_return_button.png'), device=DEV1)

