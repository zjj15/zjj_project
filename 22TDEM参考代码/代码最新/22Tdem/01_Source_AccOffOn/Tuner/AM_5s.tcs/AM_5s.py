from autost.api import *

DEV1 = ST.DEV1
checkImage = Template('')
errType = 'acc_AM5s_error'

def check(on_sleep):
    if exists(checkImage,timeout=2, device=DEV1):
        pass
    else:
        error(errType)
 
    sleep(on_sleep)
 
def playAM():
    global checkImage
    if exists(Template("pic/Tuner未播放.png"), timeout=3, threshold=ST.allSource_threshold, device=DEV1) or exists(Template("pic/Tuner播放中.png"), timeout=3, threshold=ST.allSource_threshold, device=DEV1):
        #进入Tuner
        touch([991, 384])
        #不论是不是AM在播放，都点击AM图标让AM播放
        touch([141, 571])
        sleep(1)
    checkImage = snapshot(rect=ST.eare_tuner, device=DEV1)

for i in range(2):
    keyevent(HOME, device=DEV1)
   
playAM()

#重置重启睡眠时间
ST.acc_off_sleep_time = ST.acc_off_sleep_start
#重启
do_segment(Segment('../../../common/reStart.tcs'))
#确认复归
check(ST.source_on_sleep_start)
