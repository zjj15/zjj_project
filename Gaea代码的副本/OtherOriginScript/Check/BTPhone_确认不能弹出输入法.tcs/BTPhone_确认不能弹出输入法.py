from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

print('__脚本名称: ' + __file__)


poco(className='android.widget.ImageButton', pos2=[640, 315]).assert_not_exists()
