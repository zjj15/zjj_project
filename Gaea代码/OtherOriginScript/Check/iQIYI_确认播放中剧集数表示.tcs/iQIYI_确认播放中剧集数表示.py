from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print('__脚本名称: ' + __file__)

tar_poco = poco(className='android.widget.TextView', pos2=[1600, 214]).get_attr('text')
if tar_poco is None or tar_poco=='':
    error('__脚本名称: ' + __file__+ 'Check error')
else:
    pass