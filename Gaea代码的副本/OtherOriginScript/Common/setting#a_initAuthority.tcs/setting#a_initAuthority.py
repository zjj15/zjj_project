from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

def enter_screen():
        #enter Authority page
        keyevent(HOME, device=DEV1)
        keyevent(HOME, device=DEV1)
        sleep(1)
        swipe([1414, 376],[74, 336], device=DEV1)
        sleep(1)
        swipe([1414, 376],[74, 336], device=DEV1)
        sleep(1)
        touch(Template('../../Design/More_Card.png'), device=DEV1)
        touch(Template('../../Design/Setting_Card.png'), device=DEV1)
        touch_if(Template('../../Design/setting_button.png'), device=DEV1,timeout = 5)
        touch_if(Template('../../Design/setting_Authority_icon.png'), device=DEV1,timeout = 5)
        flick_to(Template('../../Design/setting_Authority_GaoDe_icon.png'), [947, 564], DIR_DOWN, step=1, duration = 2 , speed=SPEED_NORMAL)

 
def openAuthority():
    count = 1
    while(exists(Template('../../Design/setting_Authority_off_button.png'), device=DEV1,threshold=0.8,timeout = 3)):
            touch(Template('../../Design/setting_Authority_off_button.png'), device=DEV1,threshold=0.8)
            count+=1
            if count > 6:
                break
    #for second page
    count2=1
    flick([1001, 449], DIR_UP, step=1, speed=SPEED_NORMAL)
    while(exists(Template('../../Design/setting_Authority_off_button.png'), device=DEV1,threshold=0.8,timeout = 2)):
            touch(Template('../../Design/setting_Authority_off_button.png'), device=DEV1,threshold=0.8)
            count2+=1
            if count2 > 3:
                break
    touch(Template('../../Design/setting_Authority_return_button.png'), device=DEV1,threshold=0.8)

def action():

        #first page
        touch(Template('../../Design/setting_Authority_GaoDe_icon.png'), device=DEV1,threshold=0.8)
        openAuthority()
        touch(Template('../../Design/setting_Authority_KTV_icon.png'), device=DEV1,threshold=0.8)
        openAuthority()
        touch(Template('../../Design/setting_Authority_ime_icon.png'), device=DEV1,threshold=0.8)
        openAuthority()
        touch(Template('../../Design/setting_Authority_KuGou_icon.png'), device=DEV1,threshold=0.8)
        openAuthority()
        touch(Template('../../Design/setting_Authority_AudioBook_icon.png'), device=DEV1,threshold=0.8)
        openAuthority()
        touch(Template('../../Design/setting_Authority_OnlineVideo_icon.png'), device=DEV1,threshold=0.8)
        openAuthority()
        touch(Template('../../Design/setting_Authority_icar_icon.png'), device=DEV1,threshold=0.8)
        openAuthority()

        # for second page
        flick_to(Template('../../Design/setting_Authority_carHome_icon.png'), [947, 564], DIR_UP, step=1, duration = 2 , speed=SPEED_NORMAL,timeout=120)
        touch(Template('../../Design/setting_Authority_smartFuel_icon.png'), device=DEV1,threshold=0.8)
        openAuthority()
        touch(Template('../../Design/setting_Authority_voiceAssist_icon.png'), device=DEV1,threshold=0.8,ignore_bg=True)
        openAuthority()
        touch(Template('../../Design/setting_Authority_themeShop_icon.png'), device=DEV1,threshold=0.8)
        openAuthority()
        flick_to(Template('../../Design/setting_Authority_recorder_icon.png'), [947, 564], DIR_UP, step=1, duration = 2 , speed=SPEED_NORMAL,timeout=60)
        touch(Template('../../Design/setting_Authority_recorder_icon.png'), device=DEV1,threshold=0.8)
        openAuthority() 

# delete specific file
def clear_vr():
        shell('cd navi/license/iflytek/vr/')
        res = shell('ls navi/license/iflytek/vr/')
        if res:
            print(res)
            shell('rm -rf navi/license/iflytek/vr/*')
#sleep(20)
#enter_screen()
do_segment(Segment('../../Screen/迁移到中控设定画面.tcs'))
touch_if(Template('../../Design/setting_button.png'), device=DEV1,timeout = 5)
touch_if(Template('../../Design/setting_Authority_icon.png'), device=DEV1,timeout = 5)
flick_to(Template('../../Design/setting_Authority_GaoDe_icon.png'), [947, 564], DIR_DOWN, step=1, duration = 2 , speed=SPEED_NORMAL)

action()
# case: 设备被冒用
try:
    clear_vr()
except:
    print('clear_vr error')
