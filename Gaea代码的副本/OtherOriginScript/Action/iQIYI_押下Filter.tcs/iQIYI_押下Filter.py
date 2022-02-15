from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print('__脚本名称: ' + __file__)

if exists(Template('../../Design/OnlineVideo_筛选.png'), timeout=2):
    touch(Template('../../Design/OnlineVideo_筛选.png'))
else:
    pass

try:    
    assert_exists(Template('../../Design/OnlineVideo_筛选中.png'))
except:
    error('IQIYI 押下Mine: 进入我的页面失败')
