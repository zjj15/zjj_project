from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

dict_video_name = {
    'A':ST.OnlineVideo_program_A,
    'B':ST.OnlineVideo_program_B,
    'C':ST.OnlineVideo_program_C
}
video_name = get_param('videoname')

poco_text = dict_video_name[video_name]
print('expect video_name: ',dict_video_name[video_name])

do_segment(Segment('../../Screen/进入iQIYI最近播放画面.tcs'))

recent_program_C_name = poco(className='android.widget.TextView', pos2=[238, 394]).get_attr('text')
recent_program_C_num = poco(className='android.widget.TextView', pos2=[238, 434]).get_attr('text')
recent_program_B_name = poco(className='android.widget.TextView', pos2=[468, 394]).get_attr('text')
recent_program_B_num = poco(className='android.widget.TextView', pos2=[468, 434]).get_attr('text')
recent_program_A_name = poco(className='android.widget.TextView', pos2=[698, 394]).get_attr('text')
recent_program_A_num = poco(className='android.widget.TextView', pos2=[698, 434]).get_attr('text')
prgram_C = (recent_program_C_name+recent_program_C_num).replace(" ","")
prgram_B = (recent_program_B_name+recent_program_B_num).replace(" ","")
prgram_A = (recent_program_A_name+recent_program_A_num).replace(" ","")
print('prgram_A:'+prgram_A)
print('prgram_B:'+prgram_B)
print('prgram_C:'+prgram_C)
print('expect program A:'+ST.OnlineVideo_program_A)
print('expect program B:'+ST.OnlineVideo_program_B)
print('expect program C:'+ST.OnlineVideo_program_C)

if poco_text.replace(" ","") == prgram_A:
    poco(className='android.widget.TextView', text=recent_program_A_name).click()
elif poco_text.replace(" ","") == prgram_B:
    poco(className='android.widget.TextView', text=recent_program_B_name).click()
elif poco_text.replace(" ","") == prgram_C:
    poco(className='android.widget.TextView', text=recent_program_C_name).click()
else:
    error('do nothing')