from autost.api import *

if exists(Template('../../Design/OnlineVideo_推荐_focus.png'), timeout=2):
    touch([1752, 230])
elif exists(Template('../../Design/OnlineVideo_推荐_nofocus.png'), timeout=2):
    touch(Template('../../Design/OnlineVideo_推荐_nofocus.png'), timeout=1)
    sleep(5)
else:
    error('iQIYI_播放推荐视频:不在视频播放画面')

ST.OnlineVideo_recommendation_list = 'OnlineVideo_recommendation_list.png' 
snapshot(rect=[1617, 182, 300, 309], filename= os.path.join(ST.LOG_DIR, ST.OnlineVideo_recommendation_list))

touch([1752, 230])

 
