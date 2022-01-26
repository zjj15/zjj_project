from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print('__脚本名称: ' + __file__)


try:
    poco('--:--', text='--:--', timeout=2).assert_not_exists()
    assert_exists(Template('../../Design/OnlineVideo_Progress_Bar.png'), threshold=0.90, timeout=100, device=DEV1)
except:
    error('__脚本名称: ' + __file__+ 'Check error')
