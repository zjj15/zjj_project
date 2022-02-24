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
Ipod_OFF = 'pic/Ipod_OFF.png'
Androidauto_OFF = 'pic/Androidauto_OFF.png'
Carplay_OFF = 'pic/Carplay_OFF.png'
sourceBtn=[AM_OFF, FM1_OFF, FM2_OFF, BT_OFF, USB_OFF, Ipod_OFF,Androidauto_OFF,Carplay_OFF]

def touchObj(btnObj):
    tempPic =Template('')
    if btnObj==AM_OFF:
        touchChannel()
        tempPic = snapshot(rect=ST.eare_tuner, device=DEV1)
    elif btnObj==FM1_OFF:
        touchChannel()
        tempPic = snapshot(rect=ST.eare_tuner, device=DEV1)
    elif btnObj==FM2_OFF:
        touchChannel()
        tempPic = snapshot(rect=ST.eare_tuner, device=DEV1)
    elif btnObj==BT_OFF:
        sleep(2)
        tempPic = snapshot(rect=ST.eare_devices1, device=DEV1)
    elif btnObj==USB_OFF:
        sleep(2)
        if isUSBObj:
            intoVideoView()
            if exists(Template("pic/Full_Progress.png"), timeout=0, device=DEV1):
                touch(Template("pic/Song_Choice.png"), device=DEV1)
                sleep(1)
            tempPic = snapshot(rect=ST.eare_usb_video, device=DEV1)
            keyevent(HOME, device=DEV1)
        else:
            tempPic = snapshot(rect=ST.eare_devices1, device=DEV1)

    elif btnObj==Ipod_OFF:
        tempPic = snapshot(rect=ST.eare_devices1, device=DEV1)
    else:
        error('btn error')
    return tempPic


    
    

def choiceBtn():
    btn1 = random.choice(sourceBtn)
    for i in range(choiceTimes):
        if not exists(Template(btn1), timeout=0, device=DEV1):
            btn1 = random.choice(sourceBtn)
        else:
            break
    sourceBtn.remove(btn1);
    
    TouchBtn(Template(btn1), threshold=ST.allSource_threshold, device=DEV1)

    
    btn2 = random.choice(sourceBtn)
    for i in range(choiceTimes):
        if not exists(Template(btn2), timeout=0, device=DEV1):
            btn2 = random.choice(sourceBtn)
        else:
            break
    touch(Template(btn2), device=DEV1)
    return btn1,btn2