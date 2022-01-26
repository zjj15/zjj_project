from autost.api import *

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

tar_poco_text = poco(className='android.widget.TextView',pos2=[231, 441]).get_attr('text')

if tar_poco_text is not None:
    tar_poco_text = poco(className='android.widget.TextView',pos2=[231, 441]).click()
    ST.OnlineVideo_Search_HotKeyword = poco(className='android.widget.EditText',pos2=[297, 118]).get_attr('text')
