from autost.api import *
DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print("__脚本名称: " + __file__)

do_segment(Segment('../AudioBooks_点击进入检索画面.tcs'))

touch_if(Template('../../Design/Keyboard_English_button.png'),threshold =0.8,timeout=5)

touch(Template('../../Design/Keyboard_lower_x.png'),threshold =0.8)
touch(Template('../../Design/Keyboard_lower_i.png'),threshold =0.8)
touch(Template('../../Design/Keyboard_lower_a.png'),threshold =0.8)
touch(Template('../../Design/Keyboard_lower_n.png'),threshold =0.8)
touch(Template('../../Design/Keyboard_lower_n.png'),threshold =0.8)
touch(Template('../../Design/Keyboard_lower_i.png'),threshold =0.8)

touch(Template('../../Design/IME_AudioBooks_input_xianni.png'),threshold =0.8)
touch(Template('../../Design/Keyboard_input_confirm.png'),threshold =0.8)
touch(Template('../../Design/AudioBooks_search_result_xianni.png'),threshold =0.8)


ST.AudioBooks_specbook_name = poco(className='android.widget.TextView', pos2=[1251, 407] ).get_attr('text')
ST.AudioBooks_chapter_name = poco(className='android.widget.TextView', pos2=[192, 413] ).get_attr('text')
poco(className='android.widget.TextView', pos2=[192, 413] ).click()
sleep(10)
ST.AudioBooks_pre_chapter_name = poco(className='android.widget.TextView', pos2=[192, 313] ).get_attr('text')
ST.AudioBooks_next_chapter_name = poco(className='android.widget.TextView', pos2=[192, 513] ).get_attr('text')
