from autost.api import *

poco(text='选集').click()

if not poco(className='android.widget.TextView' ,text='选集').get_attr('selected'):
    error('iQIYI_选中选集list error!!!')

