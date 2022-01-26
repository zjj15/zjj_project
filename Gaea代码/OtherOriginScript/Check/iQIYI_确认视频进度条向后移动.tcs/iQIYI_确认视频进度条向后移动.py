from autost.api import *
import time

if exists(Template('../../Design/OnlineVideo_Play_Bar.png'), threshold=0.95):
    text_progress = poco(className='android.widget.TextView', pos2=[430, 527]).get_attr('text')
    print(text_progress)
    progress_startTo = '00:00:00'
    if len(text_progress)>5:
        progress_startTo=time.strptime(text_progress,'%H:%M:%S')
    else:
        progress_startTo=time.strptime(text_progress,'%M:%S')
 
    time_diff = int(time.strftime('%H%M%S', ST.Vedio_iQIYI_progress_startTo_back)) - int(time.strftime('%H%M%S', progress_startTo))
    print('ST.time_diff:',time_diff)
    if time_diff > 10:
       pass
    else:
        error('iQIYI_确认视频进度条向后移动 error!!')

