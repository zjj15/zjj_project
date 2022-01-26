from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
DEV2 = 'GAEA_Camera:///'
print('__脚本名称: ' + __file__)

assert_exists(Template('../../Design/KTV_playing_btn.png'))

if poco(text='录音保存中，马上就好').exists():
    do_segment(Segment("../../Action/KTV_播放歌曲.tcs"))
    
    
assert_exists(Template('../../Design/KTV_playing_btn.png'))