from autost.api import *

#Action
# 手机7：A_MB_0107　号码：17301643089　蓝牙连接车机　连接IDE
# 手机2：S_MB_0569　号码：17301641459 　连接IDE
# 手机3: A_MB_0087： 号码：


#第一部拨号手机DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
DEV2 = 'iAndroid://127.0.0.1:5037/031603b3f8141501'
DEV7 = 'iAndroid://127.0.0.1:5037/DRGGAM0860501882'
 
#按打电话按钮
touch(Template('../../../Design/Phone_A_MB_0107/Diag_CallBegin.png'), device=DEV7, threshold=0.95)