from autost.api import *
print("__脚本名称: " + __file__)
#Action
# 手机7：A_MB_0107　号码：17301643089　蓝牙连接车机　连接IDE
# 手机2：S_MB_0569　号码：17301641459 　连接IDE
# 手机3: A_MB_0087： 号码：


#第一部拨号手机DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
DEV2 = 'iAndroid://127.0.0.1:5037/031603b3f8141501'
DEV7 = 'iAndroid://127.0.0.1:5037/DRGGAM0860501882'
DialNumber = '17301641459'
keyevent(HOME, device=DEV7)
keyevent(HOME, device=DEV7)

#进入拨号画面
touch_if(Template('../../../Design/Phone_A_MB_0107/PhoneBtn.png'),threshold=0.95, timeout=5, device=DEV7)

#展开拨号键盘
touch_if(Template('../../../Design/Phone_A_MB_0107/Diag_keyboard_expand_btn.png'), timeout=2, device=DEV7)
#清除残留号码
for i in range(20):
    if exists(Template('../../../Design/Phone_A_MB_0107/DialDeleteBtn.png'), timeout=2, device=DEV7, threshold=0.95):
        touch_if(Template('../../../Design/Phone_A_MB_0107/DialDeleteBtn.png'), device=DEV7, threshold=0.95)
    else:
        break


#输入电话号码
for i in range(0, len(DialNumber)):
    pic_dialNum = '../../../Design/Phone_A_MB_0107/'+'Diag_' + DialNumber[i] + '.png'
    touch(Template(pic_dialNum), device=DEV7,threshold=0.95)

