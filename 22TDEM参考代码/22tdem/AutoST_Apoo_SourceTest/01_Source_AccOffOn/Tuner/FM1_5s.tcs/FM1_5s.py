from autost.api import *

DEV1 = ST.DEV1
checkImage = Template('')
errType = 'acc_FM1_5s_error'

def check(on_sleep):
    if exists(checkImage, timeout=2, device=DEV1):
        pass
    else:
        error(errType)
        
    sleep(on_sleep)
        
def playFM1():
    global checkImage
    if exists(Template("pic/FM1_OFF.png"),timeout=1, device=DEV1):
        touch(Template("pic/FM1_OFF.png"),timeout=1, device=DEV1)
        sleep(1)
    checkImage = snapshot(rect=ST.eare_tuner, device=DEV1)

keyevent(HOME, device=DEV1)
playFM1()
#重置重启睡眠时间
ST.acc_off_sleep_time = ST.acc_off_sleep_start
#重启
do_segment(Segment("../../../common/reStart.tcs"))
#确认复归
check(ST.source_on_sleep_start)
