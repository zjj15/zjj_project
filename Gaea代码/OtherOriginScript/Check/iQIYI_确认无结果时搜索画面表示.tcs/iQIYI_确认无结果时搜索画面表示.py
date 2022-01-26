from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
#该脚本需要修改
print('__脚本名称: ' + __file__)

if poco('没有搜索到内容', text='没有搜索到内容', timeout=30).exists():
    print('有测试结果显示')
else:
    print('本次选择搜索内容有搜索结果')


touch_if(Template('../../Design/OnlineVideo_return_icon.png'), timeout=2, device=DEV1)