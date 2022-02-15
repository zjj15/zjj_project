from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print("__脚本名称: " + __file__)

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

try:    
    pwt_stop()
    pwt_send(pwt_file='./waves/Normal_OFF.pwt')
    pwt_standby(mode=0x111)
    print("pwt to play: Normal_OFF.pwt")
    pwt_play()
    print('Tbox PWT wave playing...')
    while pwt_state(wait=1) == 'play':
        print("Tbox PWT wave playing...")
    print('Tbox PWT wave playing END!')
except:
    print("pwt to play: Normal_OFF.pwt")
    error('pwt play error')
