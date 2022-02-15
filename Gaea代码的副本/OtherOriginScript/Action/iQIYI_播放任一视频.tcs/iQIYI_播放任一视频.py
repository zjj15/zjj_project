from autost.api import *
#最后状态：播放暂停

touch_if(Template('../../Design/OnlineVideo_Agreement_Confirm.png'), timeout=3)
touch_if(Template('../../Design/OnlineVideo_Login_cancel.png'), timeout=1)
touch_if(Template('../../Design/OnlineVideo_PlayScreen_return.png'), timeout=3)

if exists(Template('../../Design/OnlineVideo_走形规制_安全提示MSG.png'),threshold = 0.95, timeout = 2):
    do_segment(Segment('../CAN_发送PKB_ON.tcs'))

do_segment(Segment('../iQIYI_选择tab_tabname.tcs'), tabname='电视剧')
do_segment(Segment('../iQIYI_选中免费.tcs'))
touch([862, 352])


try:
    wait_for_appearance(Template('../../Design/OnlineVideo_Play_Bar.png'), timeout=30)
except:
    error('OnlineVideo Play Error!')

touch(Template('../../Design/OnlineVideo_return_icon.png'))
touch(Template('../../Design/OnlineVideo_Center.png'))
touch_if(Template('../../Design/OnlieVideo_Setting_View_History.png'), timeout=2)
ST.OnlineVideo_View_History = 'OnlineVideo_View_History.png' 
snapshot(rect=[241, 393, 147, 36], filename= os.path.join(ST.LOG_DIR, ST.OnlineVideo_View_History))
touch(Template('../../Design/OnlineVideo_return_icon.png'))
touch([454, 437])
sleep(5)
try:
    assert_exists(Template('../../Design/OnlineVideo_Play_Bar.png'), timeout=30,threshold = 0.9)
except:
    error('OnlineVideo_Play warning: onlinevideo play fail!')
touch_if(Template('../../Design/OnlineVideo_Playing_icon.png'), timeout=2)
ST.OnlineVideo_View_Time = 'OnlineVideo_View_Time.png'
snapshot(rect=[473, 523, 74, 39], filename= os.path.join(ST.LOG_DIR, ST.OnlineVideo_View_Time))
ST.OnlineVideo_playtime = poco(className='android.widget.TextView', pos2=[430, 527]).get_attr('text')


