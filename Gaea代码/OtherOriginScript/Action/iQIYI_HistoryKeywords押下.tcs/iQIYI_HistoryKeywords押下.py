from autost.api import *

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

key_words = get_param('keywords')
print('key_words:', key_words)

if key_words == 'withresult':
    do_segment(Segment("../iQIYI_通过Keyboard输入关键词搜索.tcs"), keywords='yi')
elif key_words == 'noresult':
    do_segment(Segment("../iQIYI_通过Keyboard输入关键词搜索.tcs"), keywords='yyyyy')
else:
    error('unknown situation')
for _ in range(2):
    touch_if(Template("../../Design/OnlineVideo_return_icon.png"), timeout=2)

do_segment(Segment("../iQIYI_Search押下.tcs"))
do_segment(Segment("../../Check/iQIYI_确认搜索画面表示.tcs"))

tar_poco_text = poco(className='android.widget.TextView',pos2=[231, 287]).get_attr('text')

if tar_poco_text is not None:
    tar_poco_text = poco(className='android.widget.TextView',pos2=[231, 287]).click()
    ST.OnlineVideo_Search_HistoryKeyword=poco(className='android.widget.EditText',pos2=[297, 118]).get_attr('text')
