from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
print("__脚本名称: " + __file__)
#3MJNPK28QCNGAUPQBS7PB278 #输入激活码step1
#FNEUAMBB82FUAD29FA39ESZM #输入激活码step2

for i in range(5):
    if exists(Template('../../Design/Statusbar_Navi_1.png'), timeout=1, threshold=0.90):
        touch(Template('../../Design/Statusbar_Navi_1.png'), timeout=3, threshold=0.90)
        break
    elif exists(Template('../../Design/Statusbar_Navi_2.png'), timeout=1, threshold=0.90):
        touch(Template('../../Design/Statusbar_Navi_2.png'), timeout=1, threshold=0.90)
        break
    elif exists(Template('../../Design/Statusbar_Navi_0.png'), timeout=1, threshold=0.90):
        touch(Template('../../Design/Statusbar_Navi_0.png'), timeout=1, threshold=0.90, device=DEV1)
        sleep(1)
    else:
        do_segment(Segment('../../Common/BackHomeView.tcs'))
        touch_if(Template('../../Design/Statusbar_Navi_0.png'), timeout=1, device=DEV1, threshold=0.90)
        sleep(1)

for i in range(3):
    touch_if(Template('../../Design/Navi_允许.png'), timeout=1, device=DEV1)
    if poco('允许', text='允许', timeout=1).exists():
        poco('允许', text='允许').click()

touch_if(Template('../../Design/GaodeNavi_Notice_neverNotice.png'), timeout=3, device=DEV1)
touch_if(Template('../../Design/GaodeNavi_Notice_agree.png'), timeout=3, device=DEV1)
touch_if(Template('../../Design/Navi_close.png'), timeout=3, device=DEV1)
touch_if(Template('../../Design/Navi_左侧弹出框.png'), timeout=1.5, threshold=0.90, device=DEV1)
#touch_if(Template('../../Design/Navi_menu_back.png'), threshold=0.93, timeout=3, device=DEV1)
#touch_if(Template('../../Design/Navi_menu_back.png'), threshold=0.93, timeout=3, device=DEV1)
while exists(Template('../../Design/Navi_menu_back.png'), timeout=3, threshold=0.93, device=DEV1):
    touch_if(Template('../../Design/Navi_menu_back.png'), timeout=3, threshold=0.93, device=DEV1)

if not exists(Template('../../Design/Navi_target.png'), threshold=0.90, device=DEV1):
    do_segment(Segment('../../Action/NAVI_结束模拟导航.tcs'))
    sleep(5)

assert_exists(Template('../../Design/Navi_target.png'), threshold=0.90)
