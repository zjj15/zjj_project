from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
for i in range(5):
    if exists(Template('../../Design/Navi_menu_back.png'), timeout=3, threshold=0.93, device=DEV1):
        touch_if(Template('../../Design/Navi_menu_back.png'), timeout=3, threshold=0.93, device=DEV1)
    else:
        break

touch_if(Template('../../Design/Navi_person_center_icon.png'), timeout=3, threshold=0.93, device=DEV1)
touch_if(Template('../../Design/Navi_offline_data_icon.png'), timeout=3, threshold=0.93, device=DEV1)
touch_if(Template('../../Design/Navi_offline_map_data_icon.png'), timeout=3, threshold=0.93, device=DEV1)
touch_if(Template('../../Design/Navi_offline_map_data_download_icon.png'), timeout=3, threshold=0.93, device=DEV1)
touch_if(Template('../../Design/Navi_offline_map_data_continue_download_icon.png'), timeout=3, threshold=0.93, device=DEV1)
wait_times = 0
while (10 >= wait_times) and (not exists(Template('../../Design/Navi_offline_map_data_download_finish_icon.png'), threshold=0.93, device=DEV1)):
    sleep(30)
    wait_times += 1

assert_exists(Template('../../Design/Navi_offline_map_data_download_finish_icon.png'), threshold=0.93, device=DEV1)
