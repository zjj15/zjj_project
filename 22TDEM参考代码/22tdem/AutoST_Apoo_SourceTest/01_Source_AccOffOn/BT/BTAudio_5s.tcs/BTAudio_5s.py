from autost.api import *

DEV1 = ST.DEV1
checkImage = Template('')
errType = 'acc_BT5s_error'

def check(on_sleep):
    if exists(checkImage,timeout=3, device=DEV1) and exists(Template('pic/BT_ON.png'),timeout=3, device=DEV1):
        pass
    else:
        error(errType)
        
    sleep(on_sleep)
        
def playBT():
    global checkImage
    if exists(Template("pic/BT_OFF.png"),timeout=1, device=DEV1):
        touch(Template("pic/BT_OFF.png"), device=DEV1)
        sleep(1)
    checkImage = snapshot(rect=ST.eare_devices2, device=DEV1)
   
keyevent(HOME, device=DEV1)
playBT()
#重置重启睡眠时间
ST.acc_off_sleep_time = ST.acc_off_sleep_start

do_segment(Segment("../../../common/reStart.tcs"))
check(ST.source_on_sleep_start)

