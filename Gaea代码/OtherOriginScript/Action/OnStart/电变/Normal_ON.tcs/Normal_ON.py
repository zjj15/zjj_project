from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'
print("__脚本名称: " + __file__)

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'

try:
    pwt_stop()
    pwt_send(pwt_file='./waves/Normal_ON.pwt')
    pwt_standby(mode=0x111)
    print("pwt to play: Normal_ON.pwt")
    pwt_play()
    print('Tbox PWT wave playing...')
    while pwt_state(wait=1) == 'play':
        print("Tbox PWT wave playing...")
    print('Tbox PWT wave playing END!')
except:
    error('pwt play error')
else:
    assert_exists(Template('../../../../Design/Home_mark_focus.png'), orv=Template('../../../../Design/Home_mark_nofocus.png'), threshold=0.92, timeout=35)
    sleep(20)
    # 消息弹出："允许讯飞输入法访问您的通讯录吗"
    for _ in range(4):
        if poco('允许', text='允许', timeout=1).exists():
            poco('允许', text='允许').click()
