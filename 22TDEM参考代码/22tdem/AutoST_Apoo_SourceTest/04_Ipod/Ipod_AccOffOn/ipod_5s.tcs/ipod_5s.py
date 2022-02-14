from autost.api import *

DEV1 = ST.DEV1
checkImage = Template('')
errType = 'acc_Ipod_error'

def check(on_sleep):
    if exists(checkImage,timeout=2, device=DEV1) and exists(Template("pic/Ipod_ON.png"), device=DEV1):
        pass
    else:
        error(errType)
        
    sleep(on_sleep)
        
def playIpod():
    global checkImage
    if exists(Template("pic/Ipod_OFF.png"),timeout=1, device=DEV1):
        touch(Template("pic/Ipod_OFF.png"), device=DEV1)
        sleep(1)
    elif exists(Template("pic/Ipod_ON.png"),timeout=1, device=DEV1):
        pass
    else:
        pring('No this button')
        end()
    checkImage = snapshot(rect=ST.eare_devices2, device=DEV1)
        
    
keyevent(HOME, device=DEV1)
playIpod()
#重置重启睡眠时间
ST.acc_off_sleep_time = ST.acc_off_sleep_start
#重启
do_segment(Segment("../../../common/reStart.tcs"))
#确认复归
check(ST.source_on_sleep_start)

