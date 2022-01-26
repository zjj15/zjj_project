from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

sleep(20)
current_charpter_name = poco(className='android.widget.TextView',pos2=[1575, 164]).get_attr('text')
if (ST.AudioBooks_pre_chapter_name == current_charpter_name):
    pass
else:
    error('AudioBooks 电子书切换到上一集失败')


