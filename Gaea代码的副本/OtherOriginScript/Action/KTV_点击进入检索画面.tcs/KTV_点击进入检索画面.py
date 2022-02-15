from autost.api import *

touch_if(Template('../../Design/KTV_mine_button.png'), timeout=3)
touch_if(Template('../../Design/KTV_song_button.png'), timeout=3)

sleep(2)
touch(Template('../../Design/OnlineVideo_Screen_Srch.png'))
sleep(1)
touch(Template('../../Design/KTV_search_inputBox.png'))

try:
    assert_exists(Template('../../Design/IME_BTPhone_keyboard_icon.png'))
except:
    error('KTV enter search screen Error!')
