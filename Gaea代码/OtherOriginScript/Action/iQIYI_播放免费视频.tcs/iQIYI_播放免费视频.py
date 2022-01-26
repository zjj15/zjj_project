from autost.api import *


if exists(Template('../../Design/OnlineVideo_走形规制_安全提示MSG.png'),threshold = 0.95, timeout = 1):
    do_segment(Segment('../DrivingRestrictOff.tcs'))

do_segment(Segment('../iQIYI_选择tab_tabname.tcs'), tabname='电视剧')
do_segment(Segment('../iQIYI_选中免费.tcs'))
touch([862, 352])
if exists(Template('../../Design/OnlineVideo_走形规制_安全提示MSG.png'),threshold = 0.95, timeout = 1):
    do_segment(Segment('../DrivingRestrictOff.tcs'))

if exists(Template('../../Design/OnlineVideo_Play_Bar.png'), timeout=35):
    pass
elif exists(Template('../../Design/OnlineVideo_暂停btn.png'), timeout=1):
    touch(Template('../../Design/OnlineVideo_暂停btn.png'), timeout=1)
elif exists(Template('../../Design/OnlineVideo_视频刷新.png'), timeout=5):
    touch(Template('../../Design/OnlineVideo_视频刷新.png'), timeout=1)
else:
    error('iQIYI_播放免费视频 error!!!')

assert_exists(Template('../../Design/OnlineVideo_Play_Bar.png'), timeout=35)
ST.OnlineVideo_program_free = poco(className='android.widget.TextView', pos2=[307, 136]).get_attr('text')
#ST.OnlineVideo_View_Time = 'OnlineVideo_View_Time.png'
#snapshot(rect=[473, 523, 74, 39], filename= os.path.join(ST.LOG_DIR, ST.OnlineVideo_View_Time))

playtime_text = poco(className='android.widget.TextView', pos2=[430, 527]).get_attr('text')
date = '2021-5-1'

if len(playtime_text)>5:
    ST.OnlineVideo_playtime = time.strptime(date + playtime_text,'%Y-%m-%d %H:%M:%S')
else:
    ST.OnlineVideo_playtime = time.strptime(date +' 00:' + playtime_text,'%Y-%m-%d %H:%M:%S')

print('ST.OnlineVideo_playtime  :',ST.OnlineVideo_playtime)
