from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

do_segment(Segment('../../Screen/进入iQIYI最近播放画面.tcs'))
recent_program_1_name = poco(className='android.widget.TextView', pos2=[238, 394]).get_attr('text')
recent_program_1_num = poco(className='android.widget.TextView', pos2=[238, 434]).get_attr('text')
recent_program_2_name = poco(className='android.widget.TextView', pos2=[468, 394]).get_attr('text')
recent_program_2_num = poco(className='android.widget.TextView', pos2=[468, 434]).get_attr('text')
recent_program_3_name = poco(className='android.widget.TextView', pos2=[698, 394]).get_attr('text')
recent_program_3_num = poco(className='android.widget.TextView', pos2=[698, 434]).get_attr('text')
prgram_C = (recent_program_1_name+recent_program_1_num).replace(" ","")
prgram_B = (recent_program_2_name+recent_program_2_num).replace(" ","")
prgram_A = (recent_program_3_name+recent_program_3_num).replace(" ","")
print('prgram_A:'+prgram_A)
print('prgram_B:'+prgram_B)
print('prgram_C:'+prgram_C)

try:
    print('expect program A:'+ST.OnlineVideo_program_A)
    assert ST.OnlineVideo_program_A.replace(" ","") == prgram_A
except:
    error(__file__+' error')

try:
    print('expect program B:'+ST.OnlineVideo_program_B)
    assert ST.OnlineVideo_program_B.replace(" ","") == prgram_B
except:
    error(__file__+' error')

try:
    print('expect program C:'+ST.OnlineVideo_program_C)
    assert ST.OnlineVideo_program_C.replace(" ","") == prgram_C
except:
    error(__file__+' error')
