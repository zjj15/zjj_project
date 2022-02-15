from autost.api import *
#任意时间剧集列表：免费综艺
print('iQIYI_播放任意时间剧集列表：免费综艺')
except_post = [1906, 209]
do_segment(Segment('../iQIYI_选择tab_tabname.tcs'), tabname='综艺')

do_segment(Segment("../iQIYI_选中免费.tcs"))

if exists(Template("../../Design/OnlineVideo_走形规制_安全提示MSG.png"),threshold = 0.95, timeout = 2):
    do_segment(Segment("../CAN_发送PKB_ON.tcs"))
touch([862, 352])
try:
    wait_for_appearance(Template("../../Design/OnlineVideo_Play_Bar.png"), timeout=30)
    for i in range(3):
        post = poco(className='android.widget.ImageView', size2=(4, 40),index=1).get_attr('pos2')
        print(post)
        if post == except_post:
            break
        flick([1783, 224], DIR_DOWN, step=3, speed=SPEED_NORMAL)
    wait_for_appearance(Template("../../Design/OnlineVideo_Play_Bar.png"), timeout=30)
    ST.OnlineVideo_variety_1st = poco(className='android.widget.TextView', pos2=[1713, 198]).get_attr('text')
    cur_program = poco(className='android.widget.TextView', pos2=[307, 136]).get_attr('text')
    if ST.OnlineVideo_variety_1st != cur_program:
        touch([1713, 198])
    cur_program = poco(className='android.widget.TextView', pos2=[307, 136]).get_attr('text')
    ST.OnlineVideo_item_list  = 'OnlineVideo_item_list.png'
    snapshot(rect=[1617, 182, 300, 309], filename= os.path.join(ST.LOG_DIR, ST.OnlineVideo_item_list))
    print('时间剧集List第一集：'+ST.OnlineVideo_variety_1st)
    print('时间剧集当前播放：'+cur_program)
except:
    error('任意时间剧集列表：免费综艺 Play Error!')
