from autost.api import *
import random

DEV1 = ST.DEV1
checkImage_btn1 = Template('')
checkImage_btn2 = Template('')
choiceTimes = 5
AM_OFF = 'pic/AM_OFF.png'
FM1_OFF = 'pic/FM1_OFF.png'
FM2_OFF = 'pic/FM2_OFF.png'
BT_OFF = 'pic/BT_OFF.png'
USB_OFF = 'pic/USB_OFF.png'
Ipod_OFF = 'pic/BT_OFF.png'
Androidauto_OFF = 'pic/Androidauto_OFF.png'
Carplay_OFF = 'pic/Carplay_OFF.png'
touchTimes = random.randint(0,3)
sourceBtn=[AM_OFF, FM1_OFF, FM2_OFF, BT_OFF, USB_OFF, Ipod_OFF,Androidauto_OFF,Carplay_OFF]

isUSBObj = random.randint(0,1)#0:Audio,1:vedio

def touchChannel():
    touchTimes = random.randint(0,3)
    for i in range(touchTimes):
        changeChannel = random.choice(['pic/Left.png', 'pic/Right.png'])
        touch(Template(changeChannel), device=DEV1)
 
def intoVideoView():
    touch(Template('pic/USB_Video.png'), device=DEV1)
    if exists(Template('pic/Video_List.png'), timeout=1, device=DEV1):
        touch(Template('pic/Video_List.png'), device=DEV1)
    else:
        touch([185, 324])
        if exists(Template('pic/Video_List.png'), timeout=1, device=DEV1):
            touch(Template('pic/Video_List.png'), device=DEV1)

def touchObj(btnObj):

    touch(Template(btnObj), device=DEV1)
    tempPic =Template('')
    if btnObj==AM_OFF:
        touchChannel()
        tempPic = snapshot(rect=ST.eare_tuner, device=DEV1)
    elif btnObj==FM1_OFF:
        touchChannel()
        tempPic = snapshot(rect=ST.eare_tuner, device=DEV1)
        #退出bt画面
        touch([151, 95])
    elif btnObj==FM2_OFF:
        touchChannel()
        tempPic = snapshot(rect=ST.eare_tuner, device=DEV1)
    elif btnObj==BT_OFF:
        sleep(2)
        tempPic = snapshot(rect=ST.eare_devices2, device=DEV1)
    elif btnObj==USB_OFF:
        sleep(2)
        if isUSBObj:
            intoVideoView()
            if exists(Template('pic/Full_Progress.png'), timeout=0, device=DEV1):
                touch(Template('pic/Song_Choice.png'), device=DEV1)
                sleep(1)
            tempPic = snapshot(rect=ST.eare_usb_video, device=DEV1)
            keyevent(HOME, device=DEV1)
        else:
            tempPic = snapshot(rect=ST.eare_devices1, device=DEV1)
    elif btnObj==Ipod_OFF:
        #ipod和carplay不能同时存在，因为iPhone手机国行版不支持。所以无法测试iPhone
        tempPic = snapshot(rect=ST.eare_devices2, device=DEV1)
    elif btnObj==Androidauto_OFF:
        tempPic = snapshot(rect=ST.eare_devices3, device=DEV1)
    elif btnObj==Carplay_OFF:
        tempPic = snapshot(rect=ST.eare_devices4, device=DEV1)   
    else:
        error('btn error')
    return tempPic

def checkSourceReturn(btnObj, image):
    touch(Template(btnObj), timeout=3, device=DEV1)
    if btnObj==USB_OFF and isUSBObj:
        touch(Template('pic/USB_Video.png'), device=DEV1)
        if not exists(image, threshold=ST.USBVideo_threshold, timeout=3, device=DEV1):
                error('Source change error')
        sleep(1)
        keyevent(HOME, device=DEV1)
    else:
        if not exists(image, timeout=5, device=DEV1):
            error('Source change error')

def choiceBtn():
    btn1 = random.choice(sourceBtn)
    for i in range(choiceTimes):
        if not exists(Template(btn1), timeout=0, device=DEV1):
            btn1 = random.choice(sourceBtn)
        else:
            break
    sourceBtn.remove(btn1);
    if btn1==BT_OFF:
        do_segment(Segment('../../01_Source_AccOffOn/BT/ConnectBT.tcs'))   
    flick([1228, 369], DIR_LEFT, step=1, speed=SPEED_NORMAL)
    flick([320, 501], DIR_RIGHT, step=1, speed=SPEED_NORMAL)
    touch(Template(btn1), device=DEV1)
    if  btn1==USB_OFF:
        usb_on(1)
    if btn1==Androidauto_OFF:
        usb_off(2)
        usb_on(2)
    if btn1==Carplay_OFF:
        usb_on(3)
    keyevent(HOME, device=DEV1)
    touch(Template('pic/菜单按钮.png'), threshold=ST.allSource_threshold)
    
    btn2 = random.choice(sourceBtn)
    for i in range(choiceTimes):
        if not exists(Template(btn2), timeout=0, device=DEV1):
            btn2 = random.choice(sourceBtn)
        else:
            break

    if btn2==BT_OFF:
        do_segment(Segment('../../01_Source_AccOffOn/BT/ConnectBT.tcs')) 
    if (btn1=='Androidauto_OFF' and btn2== 'Carplay_OFF' ) or (btn1=='Carplay_OFF' and btn2=='Androidauto_OFF'):
        print('不能同时存在')
        return None
    flick([1228, 369], DIR_LEFT, step=1, speed=SPEED_NORMAL)
    flick([320, 501], DIR_RIGHT, step=1, speed=SPEED_NORMAL)   
    touch(Template(btn2), device=DEV1)
    if  btn2==USB_OFF:
        usb_on(1)
    if btn2==Androidauto_OFF:
        usb_off(2)
        usb_on(2)
    if btn2==Carplay_OFF:
        usb_on(3)
    keyevent(HOME, device=DEV1)
    touch(Template('pic/菜单按钮.png'), threshold=ST.allSource_threshold)
    return btn1,btn2


usb_off(1)
usb_off(2)
usb_off(3)
for i in range(2):
    keyevent(HOME, device=DEV1)
touch(Template('pic/菜单按钮.png'), threshold=ST.allSource_threshold)
btnObj1, btnObj2 = choiceBtn()
for i in range(ST.touchTimes):
    #切换Source
    checkImage_btn1 = touchObj(btnObj1)
    checkImage_btn2 = touchObj(btnObj2)
    #确认Source复归
    checkSourceReturn(btnObj1, checkImage_btn1)
    checkSourceReturn(btnObj2, checkImage_btn2)


