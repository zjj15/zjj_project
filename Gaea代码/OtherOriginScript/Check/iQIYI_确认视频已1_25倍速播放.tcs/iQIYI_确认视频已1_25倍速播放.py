from autost.api import *
import time
if exists(Template('../../Design/OnlineVideo_Play_Bar.png'), threshold=0.95):
    touch([626, 543])
    sleep(8)
    touch([626, 543])
    text_progress = poco(className='android.widget.TextView', pos2=[430, 527]).get_attr('text')
    sleep(8)
    text_progress_1 = poco(className='android.widget.TextView', pos2=[430, 527]).get_attr('text')
    progress_startTo = '2021-5-1 '
    progress_startTo1 = '2021-5-1'
    print('text_progress:'+text_progress)
    print('text_progress_1'+text_progress_1)
    if len(text_progress)>5:
        progress_startTo = time.strptime(progress_startTo + text_progress,'%Y-%m-%d %H:%M:%S')
    else:
        progress_startTo = time.strptime(progress_startTo +' 00:' + text_progress,'%Y-%m-%d %H:%M:%S')

    if len(text_progress)>5:
        progress_startTo1= time.strptime(progress_startTo1 + text_progress_1,'%Y-%m-%d %H:%M:%S')
    else:
        progress_startTo1 = time.strptime(progress_startTo1 +' 00:' + text_progress_1,'%Y-%m-%d %H:%M:%S')
    print('iQIYI_确认视频1.25倍速播放_Start:', progress_startTo)
    print('iQIYI_确认视频1.25倍速播放_End:', progress_startTo1)

    #time_diff = progress_startTo - ST.Vedio_iQIYI_progress_startTo
    #time_diff = int(time.strftime('%H%M%S', progress_startTo1)) - int(time.strftime('%H%M%S', progress_startTo))
    time1= time.mktime(progress_startTo1)
    time2= time.mktime(progress_startTo)
    time_diff = time1 - time2
    print('time_diff:',time_diff)
    if time_diff>8:
       pass
    else:
        error('iQIYI_确认视频1.25倍速播放 error!!')
do_segment(Segment('../iQIYI_确认Rate为1_25.tcs'))
