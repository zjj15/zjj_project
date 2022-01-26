from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

print('__脚本名称: ' + __file__)
key_words = get_param('keywords')

if 'yi' == key_words:
    assert_exists(Template('../../Design/OnlineVideo_Such_ywy.png'), threshold=0.90, device=DEV1)
elif 'historykeywords' == key_words:
    print('ST.OnlineVideo_Search_HistoryKeyword:',ST.OnlineVideo_Search_HistoryKeyword)
    assert_exists(Template('../../Design/OnlineVideo_Such_ywy.png'), threshold=0.90, device=DEV1)
    #poco(ST.OnlineVideo_Search_HistoryKeyword, text=ST.OnlineVideo_Search_HistoryKeyword, pos2=[297, 118]).assert_exists()
elif 'hotkeywords' == key_words:
    print('ST.OnlineVideo_Search_HotKeyword:',ST.OnlineVideo_Search_HotKeyword)
    poco(ST.OnlineVideo_Search_HotKeyword, text=ST.OnlineVideo_Search_HotKeyword, pos2=[297, 118]).assert_exists()
else:
    error('invalid param')
touch_if(Template('../../Design/OnlineVideo_return_icon.png'), timeout=2, device=DEV1)