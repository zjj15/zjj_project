from autost.api import *

DEV1=ST.DEV1
DEV2 = ST.DEV2
checkImage_night = Template('')
checkImage_day = Template('')
#设置初始状态
rev_off()
ill_off()

def checkDisp(imageType='day'):
    if imageType == 'night':
        if exists(checkImage_night, timeout=1, device=DEV1):
            return True
        else:
            return False
    else:
        if exists(checkImage_day, timeout=1, device=DEV1):
            return True
        else:
            return False
            
def setError(errType):
    error(errType)

def test():
    errStr = ''
    #ILL
    errStr = "error_FM1_ill"
    ill_on()  
    if not checkDisp('night'):
        setError(errStr)
    
    ill_off()
    sleep(2)
    if not checkDisp():
        setError(errStr)
        
    #PKB+SPD
    spd_pkb()

    #REV
    do_segment(Segment("../../../common/rev_on_off.tcs"))
    
def spd_pkb():
    pkb_off()
    spd_speed(0)
    errStr = "error_SPD_PKB"
    
    #case 1:[PKB:OFF + SPD:0] SPD:0->10->0[km/h]
    sleep(1)
    spd_speed(10)
    sleep(1)

    #check into run limit
    if not checkDisp():
        setError(errStr)

    #case 2:[PKB:OFF + SPD:10] SPD:10->0[km/h]
    spd_speed(0)
    sleep(1)
    #check relieve run limit
    if not checkDisp():
        setError(errStr)
    
    #case 3:[PKB:OFF + SPD:10] SPD:10->PKN:ON[km/h]
    sleep(1)
    spd_speed(10)
    sleep(1)
    #check into run limit
    if not checkDisp():
        setError(errStr)

    pkb_on()
    #check relieve run limit
    if not checkDisp():
        setError(errStr)
        
    #case 4:[PKB:ON + SPD:0] SPD:0->10[km/h]
    #set status
    
    pkb_off()
    spd_speed(0)
    pkb_on()
    
    sleep(2)
    spd_speed(10)
    sleep(2)
    checkImage='pic/SPD_Limit.png'
    #check into run limit
    if not checkDisp():
        setError(errStr)

 

keyevent(HOME, device=DEV1)
if exists(Template("pic/Tuner未播放.png"), timeout=3, threshold=ST.allSource_threshold) or exists(Template("pic/Tuner播放中.png"), timeout=3, threshold=ST.allSource_threshold):
    #进入Tuner
    touch([991, 384])
    #不论是不是FM2在播放，都让FM2播放
    touch([444, 569])
    sleep(1)
checkImage_day = snapshot(rect=ST.eare_tuner, device=DEV1)
rev_off()
ill_on()
sleep(1)
checkImage_night = snapshot(rect=ST.eare_tuner, device=DEV1)
rev_off()
ill_on()
sleep(1)
test()
