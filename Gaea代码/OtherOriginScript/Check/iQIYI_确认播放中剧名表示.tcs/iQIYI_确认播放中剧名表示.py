from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print('__脚本名称: ' + __file__)

cur_series = poco(className='android.widget.TextView', pos2=[307, 136]).get_attr('text')
if cur_series is None or cur_series=='':
    error('__脚本名称: ' + __file__+ 'Check error')
else:
    pass    
