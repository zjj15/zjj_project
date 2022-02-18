from autost.api import *

DEV1 = ST.DEV1
ST.am +=1
checkImage = Template('')
errType = 'acc_AM_error'

def check(on_sleep):
    if exists(checkImage, timeout=2, device=DEV1):
        pass
    else:
        error(errType)
        
    sleep(on_sleep)
 
def playAM():
    global checkImage
    if exists(Template("pic/Tuner未播放.png"), timeout=3, threshold=ST.allSource_threshold) or exists(Template("pic/Tuner播放中.png"), timeout=3, threshold=ST.allSource_threshold:
        #进入Tuner
        touch([991, 384])
        #不论是不是AM在播放，都点击AM图标让AM播放
        touch([141, 571])
        sleep(1)
    checkImage = snapshot(rect=ST.eare_tuner, device=DEV1)

for i in range(2):
    keyevent(HOME, device=DEV1)
    
playAM()
onT=0
if ST.am < ST.testTimes:
    ST.acc_off_sleep_time = ST.acc_off_sleep_start + ST.am
    onT = ST.source_on_sleep_start + ST.am
else:
    ST.acc_off_sleep_time = ST.acc_off_sleep_start + ST.am
    onT = ST.source_on_sleep_start + ST.am
    ST.am = 0

do_segment(Segment('../../../common/reStart.tcs'))
check(onT)

