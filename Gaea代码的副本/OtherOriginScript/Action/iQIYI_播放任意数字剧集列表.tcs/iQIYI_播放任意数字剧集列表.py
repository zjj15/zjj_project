from autost.api import *
#任意数字剧集列表：免费电视剧
print('iQIYI_播放任意数字剧集列表：免费电视剧')
except_post = [1906, 281]
do_segment(Segment('../iQIYI_选择tab_tabname.tcs'), tabname='电视剧')

do_segment(Segment('../iQIYI_选中免费.tcs'))

if exists(Template('../../Design/OnlineVideo_走形规制_安全提示MSG.png'),threshold = 0.95, timeout = 2):
    do_segment(Segment('../CAN_发送PKB_ON.tcs'))
touch([862, 352])
try:
    wait_for_appearance(Template('../../Design/OnlineVideo_Play_Bar.png'), timeout=30)
    for i in range(3):
        post = poco(className='android.widget.ImageView', size2=(4, 58),index=1).get_attr('pos2')
        print(post)
        if post == except_post:
            break
        flick([1783, 224], DIR_DOWN, step=3, speed=SPEED_NORMAL)
    result = poco(className='android.widget.ImageView', pos2=[1616, 282]).get_attr('selected')
    print(result)
    if not result:
        #播放第一集
        poco(className='android.widget.ImageView', pos2=[1616, 282]).click()
    wait_for_appearance(Template('../../Design/OnlineVideo_Play_Bar.png'), timeout=30)
    ST.OnlineVideo_Num_1st = poco(className='android.widget.TextView', pos2=[307, 136]).get_attr('text')
    ST.OnlineVideo_Num_allNum = poco(className='android.widget.TextView', pos2=[1600, 181]).get_attr('text')
    print('数字剧集List当前播放第一集：'+ST.OnlineVideo_Num_1st)
    print('数字剧集所有集数：'+ST.OnlineVideo_Num_allNum)
    ST.OnlineVideo_item_list  = 'OnlineVideo_item_list.png'
    snapshot(rect=[1617, 182, 300, 309], filename= os.path.join(ST.LOG_DIR, ST.OnlineVideo_item_list))
 
except:
    error('任意数字剧集列表：免费电视剧 Play Error!')
