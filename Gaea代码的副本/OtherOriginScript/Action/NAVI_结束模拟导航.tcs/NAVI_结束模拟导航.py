from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
print("__脚本名称: " + __file__)

if exists(Template('../../Design/Statusbar_Navi_1.png'), timeout=1, threshold=0.90):
    pass
elif exists(Template('../../Design/Statusbar_Navi_2.png'), timeout=1, threshold=0.90):
    pass
else:
    keyevent(ITCMD_MENU)
    keyevent(ITCMD_MENU)
    poco('GPS定位中…', text='GPS定位中…').click()
    sleep(2)
if exists(Template('../../Design/Navi_naving_后_夜.png'), threshold=0.88, timeout=2) or exists(Template('../../Design/Navi_naving_后.png'), threshold=0.88, timeout=2):
    print('need to end naving')
    for i in range(10):
        if exists(Template('../../Design/Navi_menu_quitNavi.png'), timeout=1.5):
            break
        touch([755, 422])
        touch_if(Template('../../Design/Navi_naving_stop.png'), timeout=1.5, threshold=0.7)
    touch_if(Template('../../Design/Navi_menu_quitNavi.png'), timeout=1.5, threshold=0.7)
    touch_if(Template('../../Design/Navi_menu_quitNavi_夜.png'), timeout=1.5, threshold=0.7)
    touch_if(Template('../../Design/Navi_menu_quitNavi_夜2.png'), timeout=1.5, threshold=0.7)
 
    touch_if(Template('../../Design/Navi_menu_close.png'), timeout=1.5, threshold=0.93)
    touch_if(Template('../../Design/Navi_menu_back.png'), timeout=1.5, threshold=0.93)
    touch_if(Template('../../Design/Navi_menu_back.png'), timeout=1.5, threshold=0.93)
else:
    print('back to navi base screen')
    for i in range(10):
        if exists(Template('../../Design/Navi_target.png'), timeout=1.5, threshold=0.90, device=DEV1):
            break
        touch_if(Template('../../Design/Navi_naving_stop.png'), timeout=1.5, threshold=0.90)
        touch_if(Template('../../Design/Navi_menu_quitNavi.png'), timeout=1.5, threshold=0.80)
        touch_if(Template('../../Design/Navi_menu_quitNavi_夜.png'), timeout=1.5, threshold=0.8)
        touch_if(Template('../../Design/Navi_menu_quitNavi_夜2.png'), timeout=1.5, threshold=0.8)
        if exists(Template('../../Design/Navi_左侧弹出框.png'), timeout=1.5, threshold=0.90, device=DEV1):
            touch([713,394])
        touch_if(Template('../../Design/Navi_menu_close.png'), timeout=1.5, threshold=0.93)
        touch_if(Template('../../Design/Navi_menu_back.png'), timeout=1.5, threshold=0.93)
 

