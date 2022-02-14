from autost.api import *

DEV1 = ST.DEV1
ST.bt +=1
checkImage = Template('')
errType = 'acc_BT_error'

def check(on_sleep):
    if exists(checkImage, device=DEV1) and exists(Template('pic/BT_ON.png'), device=DEV1):
        pass
    else:
        error(errType)
        
    sleep(on_sleep)
        
def playBT():
    global checkImage
    if exists(Template("pic/BT_OFF.png"),timeout=1, device=DEV1):
        touch(Template("pic/BT_OFF.png"), device=DEV1)
    checkImage = snapshot(rect=ST.eare_devices2, device=DEV1)

keyevent(HOME, device=DEV1)
playBT()
onT=0
if ST.bt < ST.testTimes:
    ST.acc_off_sleep_time = ST.acc_off_sleep_start + ST.bt
    onT = ST.source_on_sleep_start + ST.bt
else:
    ST.acc_off_sleep_time = ST.acc_off_sleep_start + ST.bt
    onT = ST.source_on_sleep_start + ST.bt
    ST.bt = 0
do_segment(Segment("../../../common/reStart.tcs"))
check(onT)

