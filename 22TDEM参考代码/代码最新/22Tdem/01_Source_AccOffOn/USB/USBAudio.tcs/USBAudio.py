from autost.api import *

DEV1 = ST.DEV1
ST.usbAudio +=1
checkImage = Template('')
errType = 'acc_USB_error'

def check(on_sleep):
    if exists(checkImage, timeout=2, device=DEV1) and exists(Template("pic/USB_ON.png"), device=DEV1):
        pass
    else:
        error(errType)
        
    sleep(on_sleep)

def playUSBAudio():
    global checkImage
    if exists(Template('pic/USB_OFF.png'),timeout=1, threshold=ST.allSource_threshold, device=DEV1):
        touch(Template('pic/USB_OFF.png'),  threshold=ST.allSource_threshold, device=DEV1)
        sleep(2)
    elif exists(Template('pic/USB_ON.png'),timeout=1, threshold=ST.allSource_threshold, device=DEV1):
        pass
    else:
        error("No find the view")
    checkImage = snapshot(rect=ST.eare_devices2, device=DEV1)

usb_on(1)
for i in range(2):
    keyevent(HOME, device=DEV1)
touch(Template('pic/菜单按钮.png'), threshold=ST.allSource_threshold)
playUSBAudio()
onT=0
if ST.usbAudio < ST.testTimes:
    ST.acc_off_sleep_time = ST.acc_off_sleep_start + ST.usbAudio
    onT = ST.source_on_sleep_start + ST.usbAudio
else:
    ST.acc_off_sleep_time = ST.acc_off_sleep_start + ST.usbAudio
    onT = ST.source_on_sleep_start + ST.usbAudio
    ST.usbAudio = 0
end()
do_segment(Segment("../../../common/reStart.tcs"))
check(onT)


