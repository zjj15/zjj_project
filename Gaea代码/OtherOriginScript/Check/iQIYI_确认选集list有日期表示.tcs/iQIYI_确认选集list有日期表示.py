from autost.api import *

program_date = poco(className='android.widget.TextView', pos2=[1713, 228]).get_attr('text')
print('选集list Item日期：'+program_date)

if program_date is None or program_date=='':
    error('iQIYI_确认选集栏有日期表示 error!!!')
