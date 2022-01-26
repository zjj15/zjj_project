from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

ST.delete_program_1_name = poco(className='android.widget.TextView', pos2=[238, 394]).get_attr('text')
ST.delete_program_1_num = poco(className='android.widget.TextView', pos2=[238, 434]).get_attr('text')
poco('android.widget.ImageView', pos2=[283, 504]).click()#Template('../../Design/OnlineVideo_我的收藏_删除icon.png')
sleep(0.5)
