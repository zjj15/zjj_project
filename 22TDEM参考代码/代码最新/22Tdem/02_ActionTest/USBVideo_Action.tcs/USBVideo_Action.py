from autost.api import *

DEV1 = ST.DEV1
DEV2 = ST.DEV2
checkImage_Default = 'pic/Video_On.png'
sendCAN(MICU_BCM.C_BACKLTSW.phys,0.0, interval=0.1, device=DEV1)
sendCAN(ILLUMI.C_METER_ILL_STATUS.phys,0.0, interval=0.1, device=DEV1)
spd_speed(0)

def checkDisp(checkImage=checkImage_Default):
    
    if exists(Template(checkImage), timeout=1, device=DEV1):
        return True
    else:
        return False
        
def setError(errType):
    error(errType)

def test():
    errStr = ''
    #ILL
    errStr = "error_USBVideo_ill"
    sendCAN(MICU_BCM.C_IG1.phys,1.0, interval=0.1, device=DEV1)
    sendCAN(ILLUMI.C_METER_ILL_STATUS.phys,1.0, interval=0.1, device=DEV1)
    sleep(2)

    if not checkDisp('pic/ILL_On_Video_On.png'):
        setError(errStr)
    
    sendCAN(ILLUMI.C_METER_ILL_STATUS.phys,0.0, interval=0.1, device=DEV1)
    sleep(2)
    if not checkDisp():
        setError(errStr)

    #SPD+PKB
    spd_pkb()
    
    #REV
    do_segment(Segment("../../common/rev_on_off.tcs"))

def spd_pkb():
    sendCAN(MICU_BCM.C_IG1.phys,1.0, interval=0.1, device=DEV1)
    sendCAN(AT.C_PBRAKE.phys,0.0, interval=0.1, device=DEV1)
    spd_speed(0)

    #case 1:[PKB:OFF + SPD:0] SPD:0->55->0[km/h]
    sleep(1)
    spd_speed(55)
    sleep(1)
    errStr = "error_SPD_PKB"
    checkImage='pic/SPD_Limit.png'
    #check into run limit
    if not checkDisp(checkImage):
        setError(errStr)

    #case 2:[PKB:OFF + SPD:55] SPD:55->0[km/h]
    spd_speed(0)
    sleep(1)
    #check relieve run limit
    if checkDisp(checkImage) and not checkDisp():
        setError(errStr)
    
    #case 3:[PKB:OFF + SPD:55] SPD:55->PKN:ON[km/h]
    sleep(1)
    spd_speed(55)
    sleep(1)
    errStr = "error_SPD_PKB"
    checkImage='pic/SPD_Limit.png'
    #check into run limit
    if not checkDisp(checkImage):
        setError(errStr)

    sendCAN(MICU_BCM.C_IG1.phys,1.0, interval=0.1, device=DEV1)
    sendCAN(AT.C_PBRAKE.phys,1.0, interval=0.1, device=DEV1)
    #check relieve run limit
    if checkDisp(checkImage) and not checkDisp():
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
    errStr = "error_SPD_PKB"
    checkImage='pic/SPD_Limit.png'
    #check into run limit
    if checkDisp(checkImage):
        setError(errStr)

keyevent(HOME, device=DEV1)
if exists(Template('pic/USB_OFF.png'), timeout=1, device=DEV1):
    touch(Template('pic/USB_OFF.png'), device=DEV1)
    touch(Template("pic/USB_Video.png"), device=DEV1)
   
else:
    touch(Template("pic/USB_Video.png"), device=DEV1)
    
if exists(Template('pic/Video_List.png'), device=DEV1):
    touch(Template('pic/Video_List.png'), device=DEV1)
else:
    touch([185, 324])
    if exists(Template('pic/Video_List.png'), device=DEV1):
        touch(Template('pic/Video_List.png'), device=DEV1)

if exists(Template('pic/Full_Progress.png'), timeout=0, device=DEV1):
    touch(Template('pic/Song_Choice.png'), device=DEV1)
        
test()
        

