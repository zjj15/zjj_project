from autost.api import *
import time
if exists(Template('../../Design/OnlineVideo_Play_Bar.png'), threshold=0.95) or exists(Template("../../Design/OnlineVideo_暂停状态.png"),threshold = 0.95):
    touch([632, 546])
    text_progress = poco(className='android.widget.TextView', pos2=[430, 527]).get_attr('text')
    print(text_progress)
    if len(text_progress)>5:
        ST.Vedio_iQIYI_progress_startTo=time.strptime(text_progress,'%H:%M:%S')
    else:
        ST.Vedio_iQIYI_progress_startTo=time.strptime(text_progress,'%M:%S')
    print('ST.Vedio_iQIYI_progress_startTo:',ST.Vedio_iQIYI_progress_startTo)

    flick([711, 455], DIR_RIGHT, step=3, speed=SPEED_NORMAL)
    flick([711, 455], DIR_RIGHT, step=3, speed=SPEED_NORMAL)
    text_progress1 = poco(className='android.widget.TextView', pos2=[430, 527]).get_attr('text')
    #text_progress1 = image_to_string([462, 521, 89, 39])
    print('text_progress1:',text_progress1)
 
else:
    error('iQIYI_视频向前滑动:不在视频播放状态')
 
