from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

while exists(Template('../../Design/Navi_menu_back.png'), timeout=3, threshold=0.93, device=DEV1):
    touch_if(Template('../../Design/Navi_menu_back.png'), timeout=3, threshold=0.93, device=DEV1)

touch_or(Template('../../Design/Navi_mine_button_夜.png'), Template('../../Design/Navi_person_center_icon.png'), timeout=3, threshold=0.93, device=DEV1)
touch_if(Template('../../Design/Navi_setting_icon.png'), timeout=3, threshold=0.93, device=DEV1)
sleep(1)
for _ in range(5):
    touch([65, 510])
    if exists(Template("../../Design/Navi_地图模式_夜_选中.png"), timeout=1) or exists(Template("../../Design/Navi_地图模式_夜_未选中.png"), timeout=1):
        break
    if exists(Template("../../Design/Navi_setting_日夜模式text.png"), timeout=1):
        swipe([800,608],[800,515],steps=10)
for i in range(3):
    touch_if(Template("../../Design/Navi_地图模式_夜_未选中.png"), timeout=2)
    if exists(Template("../../Design/Navi_地图模式_夜_选中.png"), timeout=1):
        break