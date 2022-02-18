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
    sendCAN(MICU_BCM.C_IG1.phys,1.0, interval=0.1, device=DEV1)
    sendCAN(ILLUMI.C_METER_ILL_STATUS.phys,1.0, interval=0.1, device=DEV1)
  
    if not checkDisp('night'):
        setError(errStr)
    
    sendCAN(ILLUMI.C_METER_ILL_STATUS.phys,0.0, interval=0.1, device=DEV1)
    sleep(2)
    if not checkDisp():
        setError(errStr)
        
    #PKB+SPD
    spd_pkb()

    #REV
    do_segment(Segment("../../../common/rev_on_off.tcs"))
    
def spd_pkb():
    sendCAN(MICU_BCM.C_IG1.phys,1.0, interval=0.1, device=DEV1)
    sendCAN(AT.C_PBRAKE.phys,0.0, interval=0.1, device=DEV1)
    spd_speed(0)
    errStr = "error_SPD_PKB"
    
    #case 1:[PKB:OFF + SPD:0] SPD:0->55->0[km/h]
    sleep(1)
    spd_speed(55)
    sleep(1)

    #check into run limit
    if not checkDisp():
        setError(errStr)

    #case 2:[PKB:OFF + SPD:55] SPD:55->0[km/h]
    spd_speed(0)
    sleep(1)
    #check relieve run limit
    if not checkDisp():
        setError(errStr)
    
    #case 3:[PKB:OFF + SPD:55] SPD:55->PKN:ON[km/h]
    sleep(1)
    spd_speed(55)
    sleep(1)
    #check into run limit
    if not checkDisp():
        setError(errStr)

    sendCAN(MICU_BCM.C_IG1.phys,1.0, interval=0.1, device=DEV1)
    sendCAN(AT.C_PBRAKE.phys,1.0, interval=0.1, device=DEV1)
    #check relieve run limit
    if not checkDisp():
        setError(errStr)
        
    #case 4:[PKB:ON + SPD:0] SPD:0->55[km/h]
    #set status
    sendCAN(MICU_BCM.C_IG1.phys,1.0, interval=0.1, device=DEV1)
    sendCAN(AT.C_PBRAKE.phys,0.0, interval=0.1, device=DEV1)
    spd_speed(0)
    sendCAN(AT.C_PBRAKE.phys,1.0, interval=0.1, device=DEV1)
    
    sleep(2)
    spd_speed(55)
    sleep(2)
    checkImage='pic/SPD_Limit.png'
    #check into run limit
    if not checkDisp():
        setError(errStr)
 
keyevent(HOME, device=DEV1)
if exists(Template('pic/FM1_OFF.png'), timeout=1, device=DEV1):
    touch(Template('pic/FM1_OFF.png'), timeout=1, device=DEV1)
    sleep(1)
    
checkImage_day = snapshot(rect=ST.eare_tuner, device=DEV1)
sendCAN(MICU_BCM.C_BACKLTSW.phys,0.0, interval=0.1, device=DEV1)
sendCAN(ILLUMI.C_METER_ILL_STATUS.phys,1.0, interval=0.1, device=DEV1)
sleep(1)
checkImage_night = snapshot(rect=ST.eare_tuner, device=DEV1)
sendCAN(MICU_BCM.C_BACKLTSW.phys,0.0, interval=0.1, device=DEV1)
sendCAN(ILLUMI.C_METER_ILL_STATUS.phys,0.0, interval=0.1, device=DEV1)
sleep(1)
test()

