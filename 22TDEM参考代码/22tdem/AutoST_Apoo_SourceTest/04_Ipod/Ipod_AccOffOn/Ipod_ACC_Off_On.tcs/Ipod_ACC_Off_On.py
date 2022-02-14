from autost.api import *

DEV1 = ST.DEV1
ST.ipod +=1
checkImage = Template('')
errType = 'acc_Ipod_5s_error'

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
onT=0
if ST.ipod < ST.testTimes:
    ST.acc_off_sleep_time = ST.acc_off_sleep_start + ST.ipod
    onT = ST.source_on_sleep_start + ST.ipod
else:
    ST.acc_off_sleep_time = ST.acc_off_sleep_start + ST.ipod
    onT = ST.source_on_sleep_start + ST.ipod
    ST.ipod = 0
    
do_segment(Segment('../../../common/reStart.tcs'))

check(onT)


