from autost.api import *

DEV1 = ST.DEV1
DEV2 = ST.DEV2

checkImage_night1 = Template('')
checkImage_night2 = 'pic/WireCarplay_On_night.png'
checkImage_day1 = Template('') #ill off
checkImage_day2 = 'pic/WireCarplay_On_day.png' #ill off
rev_off()
ill_off()
spd_speed(0)

def checkDisp(imageType='day'):
    if imageType == 'night':
        if exists(checkImage_night1, threshold=ST.allSource_threshold, device=DEV1) and exists(Template(checkImage_night2), threshold=ST.allSource_threshold, device=DEV1):
            return True
        else:
            return False
    else:
        if exists(checkImage_day1, threshold=ST.allSource_threshold, device=DEV1) and exists(Template(checkImage_day2), threshold=ST.allSource_threshold, device=DEV1):
            return True
        else:
            return False
 
def setError(errType):
    error(errType)

def test():
    errStr = ''
    #ILL
    errStr = "error_BT_ill"
    ill_on()
 
    if not checkDisp('night'):
        setError(errStr)
 
    #sendCAN(ILLUMI.C_METER_ILL_STATUS.phys,0.0, interval=0.1, device=DEV1)
    ill_off()
    sleep(2)
    if not checkDisp():
        setError(errStr)
 
    #PKB+SPD
    spd_pkb()

    #REV
    do_segment(Segment('../../common/rev_on_off.tcs'))
 
def spd_pkb():
    pkb_on()
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
 
if exists(Template('pic/WireCp_Connected.png'), threshold=ST.allSource_threshold, device=DEV1):
    #进入carplay画面
    touch([307, 378])
    #播放音乐
    touch_if(Template('pic/音乐图标.png'), threshold=ST.allSource_threshold, device=DEV1)
    touch_if(Template('pic/播放中.png'), threshold=ST.allSource_threshold, device=DEV1)
    if exists(Template('pic/播放按钮.png'), threshold=ST.allSource_threshold, device=DEV1):
        touch(Template('pic/播放按钮.png'), threshold=ST.allSource_threshold, device=DEV1)
    else:
        pass
    sleep(1)
checkImage_day1 = snapshot(rect=ST.eare_devices3, device=DEV1)
rev_off()
ill_on()
checkImage_night1 = snapshot(rect=ST.eare_devices3, device=DEV1)
spd_speed(0)
rev_off()
ill_off()
test()

