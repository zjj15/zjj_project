from autost.api import *

if exists(Template("../../Design/OnlineVideo_Play_Bar.png"), threshold=0.95):
    sleep(2)
    text_progress = image_to_string([462, 521, 89, 39])
    print(text_progress)
    progress_startTo = '00:00:00'
    if len(text_progress)>5:
        progress_startTo=time.strptime(text_progress,'%H:%M:%S')
    else:
        progress_startTo=time.strptime(text_progress,'%M:%S')
    #time_diff = progress_startTo - ST.Vedio_iQIYI_progress_startTo
    time_diff = int(time.strftime('%H%M%S', progress_startTo)) - int(time.strftime('%H%M%S', ST.Vedio_iQIYI_progress_startTo))
    print('ST.time_diff:',time_diff)
    if time_diff > 1:
       pass
    else:
        error('iQIYI_确认视频进度条向前移动 error！！！')
assert_exists(Template("../../Design/OnlineVideo_Play_Bar.png"), threshold=0.95)