from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

if poco(text='取消').exists():
    poco(text='取消').click()

touch_if(Template('../../Design/NissanRadio_return_button.png'), timeout=3, threshold=0.8)

touch_if(Template('../../Design/NissanRadio_search_button.png'), timeout=5)

#touch(Template('../../Design/NissanRadio_search_inputBox.png'))

poco(text='搜索专辑、直播、声音、主播、广播').click()



try:
    assert_exists(Template('../../Design/IME_BTPhone_keyboard_icon.png'))
except:
    error('NissanRadeo enter search screen Error!')
