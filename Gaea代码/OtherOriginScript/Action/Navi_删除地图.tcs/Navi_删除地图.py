from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

while exists(Template('../../Design/Navi_menu_back.png'), timeout=3, threshold=0.93, device=DEV1):
    touch_if(Template('../../Design/Navi_menu_back.png'), timeout=3, threshold=0.93, device=DEV1)

touch_if(Template('../../Design/Navi_person_center_icon.png'), timeout=3, threshold=0.93, device=DEV1)
touch_if(Template('../../Design/Navi_offline_data_icon.png'), timeout=3, threshold=0.93, device=DEV1)
touch_if(Template('../../Design/Navi_offline_map_data_icon.png'), timeout=3, threshold=0.93, device=DEV1)
touch_if(Template('../../Design/Navi_offline_map_data_manage_icon.png'), timeout=3, threshold=0.93, device=DEV1)
touch_if(Template('../../Design/Navi_offline_map_data_downloaded_menu.png'), timeout=3, threshold=0.93, device=DEV1)
touch_if(Template('../../Design/Navi_offline_map_data_baseFunctionPackage.png'), timeout=3, threshold=0.93, device=DEV1)
touch_if(Template('../../Design/Navi_offline_map_data_delete_icon.png'), timeout=3, threshold=0.93, device=DEV1)
