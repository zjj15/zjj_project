from autost.api import *

if exists(Template("../../Design/OnlineVideo_Play_Bar.png"), threshold=0.95):
    touch([626, 543])
    flick([626, 540], DIR_RIGHT, step=1, speed=SPEED_NORMAL)
    text_progress = image_to_string([462, 521, 89, 39])
    if len(text_progress)>5:
        ST.Vedio_iQIYI_progress_startTo=time.strptime(text_progress,'%H:%M:%S')
    else:
        ST.Vedio_iQIYI_progress_startTo=time.strptime(text_progress,'%M:%S')
    print('ST.Vedio_iQIYI_progress_startTo:',ST.Vedio_iQIYI_progress_startTo)
