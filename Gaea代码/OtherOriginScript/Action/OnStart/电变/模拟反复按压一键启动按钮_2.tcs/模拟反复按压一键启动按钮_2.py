from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print("__脚本名称: " + __file__)

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
## INFO: check pwt playing
## C1A-HS电源状态如下
## value of T depending on the pwt file currently running
##
## ---10ms-----|---------T---------|----s-----|---10ms---
##             |                   |          |
##   MMI OFF  ->       ON STATUS


pwt_list=[
 'Push SW2_24ms',
 'Push SW2_42ms',
 'Push SW2_60ms'
]
def check_pwt_playing(rand_idx):
    start_time = time.time()
    print('strt_time:',time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    if 0 == rand_idx:
        sleep_sec=0.024*5+2*4
    elif 1 == rand_idx:
        sleep_sec=0.042*5+2*4
    elif 2 == rand_idx:
        sleep_sec=0.060*5+2*4
    else:
        print('do nothing')

    ##------------------------
    ## check pwt playing Start
    ## 
    assert_exists(Template("../../../../Design/Home_mark_nofocus.png"), orv=Template("../../../../Design/Home_mark_focus.png"), timeout=1, threshold=0.90)
    current_time = time.time()
    wait_time = 0.01 + sleep_sec - (current_time - start_time)
    if wait_time > 0:
        sleep(wait_time)
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    ##----------------------
    ## check pwt playing END

import random
rand_idx = random.randint(0,len(pwt_list)-1)
print('rand_idx:',rand_idx)
pwt_to_play = pwt_list[rand_idx]

current_screen = snapshot(rect=[15, 15, 450, 60], device=DEV1)
try:
    if pwt_to_play:
        pwt_stop()
        pwt_send(pwt_file='./waves/%s.pwt'%pwt_to_play)
        pwt_standby(mode=0x111)
        print("pwt to play: ", pwt_to_play)
        pwt_play()
        if pwt_state() == "play":
            print('Tbox PWT wave playing...')
        else:
            print("not play")
        ## check pwt playing Start
        check_pwt_playing(rand_idx)
        while pwt_state(wait=1) == 'play':
            print("Tbox PWT wave playing...")
        print('Tbox PWT wave playing END!')
except:
    print("pwt to play: ", pwt_to_play)
    error('pwt play error')
else:
    assert_exists(current_screen)
