from autost.api import *
#前提条件：之前有播放过视频
touch_if(Template('../../Design/OnlineVideo_Login_cancel.png'), timeout=1)

assert_exists(Template('../../Design/OnlineVideo_Play_Bar.png'), timeout=30)
video_program = poco(className='android.widget.TextView', pos2=[307, 136]).get_attr('text')
if video_program != ST.OnlineVideo_program_free:
    error('iQIYI_确认播放之前的视频 error!!!')
