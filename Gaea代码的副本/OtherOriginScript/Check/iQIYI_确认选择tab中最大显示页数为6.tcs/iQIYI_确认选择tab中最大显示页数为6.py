from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
DEV2 = 'GAEA_Camera:///'
print('__脚本名称: ' + __file__)

tab_name = get_param('tabname')
print('tab_name: %s,'%(tab_name))
max_page_num = 6

for i in range(max_page_num): 
    if 0 == i:
        snp_cur_screen = snapshot(rect=[231, 281, 480, 360])
    poco('android.widget.ImageView', pos2=[634, 423]).click()
    if exists(snp_cur_screen, timeout=1.5):
        break
else:
    error('__脚本名称: ' + __file__+ 'Check error')

