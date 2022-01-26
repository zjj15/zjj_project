from autost.api import *
import time

if exists(Template('../../Design/OnlineVideo_Play_Bar.png'), threshold=0.95) or exists(Template('../../Design/OnlineVideo_暂停状态.png'),threshold = 0.95):
    touch([657, 543])
    text_progress = poco(className='android.widget.TextView', pos2=[430, 527]).get_attr('text')
    print('iQIYI_视频向后滑动前:'+text_progress)
    if len(text_progress)>5:
        ST.Vedio_iQIYI_progress_startTo_back=time.strptime(text_progress,'%H:%M:%S')
    else:
        ST.Vedio_iQIYI_progress_startTo_back=time.strptime(text_progress,'%M:%S')
    print('ST.Vedio_iQIYI_progress_startTo_back:',ST.Vedio_iQIYI_progress_startTo_back)
    sleep(5)
    flick([1224, 383], DIR_LEFT, step=1, speed=SPEED_NORMAL)
    flick([1224, 383], DIR_LEFT, step=1, speed=SPEED_NORMAL)
    text_progress1 = poco(className='android.widget.TextView', pos2=[430, 527]).get_attr('text')
    print('iQIYI_视频向后滑动之后:',text_progress1)

