from autost.api import *

while exists(Template('../../Design/AudioBooks_back_icon.png'), timeout=3, threshold=0.93):
    touch_if(Template('../../Design/AudioBooks_back_icon.png'), timeout=3, threshold=0.93)

touch_if(Template('../../Design/AudioBooks_search_cancel_button.png'),timeout=3)
sleep(1)
touch(Template('../../Design/AudioBooks_search_button.png'))
sleep(1)
touch(Template('../../Design/AudioBooks_search_inputBox.png'))

try:
    assert_exists(Template('../../Design/IME_BTPhone_keyboard_icon.png'))
except:
    error('AudioBooks enter search screen Error!')
