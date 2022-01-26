from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print("__脚本名称: " + __file__)

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
## INFO: check pwt playing
## C1A-HS电源状态如下
## value of T depending on the pwt file currently running
##
## ----10ms-----|(--T1--T2--)*(5 times)|---500ms---|(--T1--T2--)*(5 times)|---500ms---
##              |                      |           |                      |
##   MMI OFF   ->                       ON STATUS


pwt_list=[
 'IGN_ON-OFF100_10',   #0.55
 'IGN_ON-OFF100_100',  #1
 #'IGN_ON-OFF10_10',    #0.05
 'IGN_ON-OFF10_100',   #0.55
 'IGN_ON-OFF150_10',   #0.8
 'IGN_ON-OFF150_100',  #1.25
 'IGN_ON-OFF200_10',   #1.05
 'IGN_ON-OFF200_100',  #1.5
 'IGN_ON-OFF300_10',   #1.55
 'IGN_ON-OFF300_100',  #2
 'IGN_ON-OFF400_10',   #2.05
 'IGN_ON-OFF400_100',  #2.5
 'IGN_ON-OFF50_10',    #0.3
 'IGN_ON-OFF50_100'    #0.75
]

def get_sleep_sec(pwt_name):
    idx = len('IGN_ON-OFF')
    split_list = pwt_name[idx:].split('_')
    #print(split_list)
    sec=0
    for t in split_list:
        sec+=float(t)
    sec = sec*5/1000
    print('sec:',sec)
    return sec

def check_pwt_playing(rand_idx):
    start_time = None
    if pwt_state() == "play":
        print('Tbox PWT wave playing...')
        start_time = time.time()
        print('strt_time:', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    else:
        print(pwt_state())
        error("Tbox PWT wave not play")
    sleep_sec=get_sleep_sec(pwt_list[rand_idx])

    ##------------------------
    ## check pwt playing Start
    ## 1,MMI OFF
    current_time = time.time()
    wait_time = 0.01 - (current_time - start_time)
    if wait_time > 0:
        sleep(wait_time)
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    ## 2,ON STATUS, sleep_sec
    #TODO：补充check项
    current_time = time.time()
    wait_time = 1.01 + 2*sleep_sec - (current_time - start_time)
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
        pwt_name = pwt_list[rand_idx]
        pwt_play()
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
