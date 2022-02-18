from autost.api import *

DEV1 = ST.DEV1
checkImage = Template('')
errType = 'acc_BT5s_error'

def check(on_sleep):
    if exists(checkImage,timeout=3, threshold=ST.allSource_threshold, device=DEV1):
        pass
    else:
        error(errType)
 
    sleep(on_sleep)
 
def playBT():
    global checkImage
    #不论BT off n 都进入bt audio画面
    touch(Template('pic/BT图标.png'), threshold=ST.allSource_threshold)
    if exists(Template('pic/BtMusic_确认播放.png'), threshold=ST.allSource_threshold):
        print('playing bt music')
    else:
        error(errType)
        
    checkImage = snapshot(rect=ST.eare_devices2, device=DEV1)

for i in range(2):
    keyevent(HOME, device=DEV1)

touch(Template("pic/菜单按钮.png"), threshold=ST.allSource_threshold)
playBT()
#重置重启睡眠时间
ST.acc_off_sleep_time = ST.acc_off_sleep_start
do_segment(Segment('../../../common/reStart.tcs'))
check(ST.source_on_sleep_start)

