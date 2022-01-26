from autost.api import *
#iQIYI_播放任意无剧集列表的视频:免费电影
print('iQIYI_播放任意无剧集列表的视频:免费电影')

do_segment(Segment('../iQIYI_选择tab_tabname.tcs'), tabname='电影')

do_segment(Segment('../iQIYI_选中免费.tcs'))

if exists(Template('../../Design/OnlineVideo_走形规制_安全提示MSG.png'),threshold = 0.95, timeout = 2):
    do_segment(Segment('../CAN_发送PKB_ON.tcs'))
touch([862, 352])
try:
    wait_for_appearance(Template('../../Design/OnlineVideo_Play_Bar.png'), timeout=30)

    ST.OnlineVideo_movie = poco(className='android.widget.TextView', pos2=[307, 136]).get_attr('text')
    ST.OnlineVideo_relevant = poco(className='android.widget.TextView', pos2=[1713, 198]).get_attr('text')
    ST.OnlineVideo_item_list  = 'OnlineVideo_item_list.png'
    snapshot(rect=[1617, 182, 300, 309], filename= os.path.join(ST.LOG_DIR, ST.OnlineVideo_item_list))
 
    print('任意无剧集列表的视频电影：'+ST.OnlineVideo_movie)
except:
    error('免费电影 Play Error!')
