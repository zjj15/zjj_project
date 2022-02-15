from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
DEV2 = 'GAEA_Camera:///'
print('__脚本名称: ' + __file__)

try:
    assert_exists(Template('../../Design/Camera/KuGou_ILLOFF_menubar.png'), threshold=0.70, device=DEV2)
    assert_exists(Template('../../Design/Camera/KuGou_ILLOFF_home.png'), threshold=0.70, device=DEV2)
except:
    error('__脚本名称: ' + __file__+ 'Check error')
 
