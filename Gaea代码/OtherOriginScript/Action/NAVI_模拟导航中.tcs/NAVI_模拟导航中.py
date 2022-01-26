from autost.api import *
DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
print("__脚本名称: " + __file__)

if exists(Template('../../Design/Navi_target.png'), threshold=0.90, timeout=3, device=DEV1):
    pass
else:
    do_segment(Segment('../../Screen/迁移到NAVI画面.tcs'))

## 模拟导航开始
touch(Template('../../Design/Navi_target.png'), threshold=0.90, device=DEV1)
for _ in range(3):
    touch_if(Template('../../Design/Navi_searchBar.png'), timeout=1.5, threshold=0.93)
    sleep(1.5)
    if exists(Template('../../Design/Navi_搜索_Keyboard_首拼.png'), timeout=1.5, threshold=0.90):
        touch(Template('../../Design/Navi_搜索_Keyboard_首拼.png'), timeout=1.5, threshold=0.90)
        touch(Template('../../Design/Navi_搜索_Keyboard_拼音.png'), timeout=1.5, threshold=0.90)
 
    if exists(Template('../../Design/Navi_搜索_Keyboard_d.png'), timeout=2, threshold=0.94):
        break

if exists(Template('../../Design/Navi_search_history.png'), timeout=2, threshold=0.94):
    touch(Template('../../Design/Navi_search_history.png'), threshold=0.94)
else:
    touch(Template('../../Design/Navi_搜索_Keyboard_d.png'), threshold=0.94)
    touch(Template('../../Design/Navi_搜索_Keyboard_f.png'), threshold=0.94)
    touch(Template('../../Design/Navi_搜索_Keyboard_m.png'), threshold=0.94)
    touch(Template('../../Design/Navi_搜索_Keyboard_z.png'), threshold=0.94)
    touch(Template('../../Design/input_search_dfmz.png'), threshold=0.94)
    sleep(5)
    touch_if(Template('../../Design/Navi_search_result.png'), threshold=0.90)
    sleep(3)

touch(Template('../../Design/Navi_menu_gotohere.png'), threshold=0.93)
touch(Template('../../Design/Navi_menu_more.png'), threshold=0.93)
touch(Template('../../Design/Navi_menu_SimulationNavigation.png'), threshold=0.93)

