from autost.api import *
DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print("__脚本名称: " + __file__)

ST.AudioBooks_book_name = None

for _ in range(5):
    touch_if(Template('../../Design/AudioBooks_pause_btn.png'), timeout=2)
    if exists(Template('../../Design/AudioBooks_playing_btn.png'), timeout=5):
        break
else:
    error('wifi signal bad: audiobooks play failed!')
# 三方app，式样变更
ST.AudioBooks_book_name = poco(className='android.widget.TextView', pos2=[1580, 164] ).get_attr('text')
print('ST.AudioBooks_book_name', ST.AudioBooks_book_name)


