from autost.api import *

DEV1 = ST.DEV1
ST.am +=1
checkImage = Template('')
errType = 'acc_AndroidAuto_error'

def check(on_sleep):
    if exists(checkImage,timeout=10, device=DEV1):
        pass
    else:
        error(errType)
    sleep(on_sleep)

def playAndroidAuto():
    global checkImage
    if exists(Template("pic/AA_连接成功.png"), threshold=ST.allSource_threshold, device=DEV1) :
        print('AA_连接成功')
    elif exists(Template("pic/AndroidAuto卡片.png")):
        touch([299, 337])
        sleep(5)
    checkImage = snapshot(rect=ST.eare_devices3, device=DEV1)
      

for i in range(2):
    keyevent(HOME, device=DEV1)
usb_on(2)
playAndroidAuto()

onT=0
if ST.am < ST.testTimes:
    ST.acc_off_sleep_time = ST.acc_off_sleep_start + ST.am
    onT = ST.source_on_sleep_start + ST.am
else:
    ST.acc_off_sleep_time = ST.acc_off_sleep_start + ST.am
    onT = ST.source_on_sleep_start + ST.am
    ST.am = 0
    
#确认复归
check(onT)
usb_off(2)