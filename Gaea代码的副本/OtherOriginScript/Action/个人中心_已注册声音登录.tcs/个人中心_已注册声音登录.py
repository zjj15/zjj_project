from autost.api import *

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
#车型：P42Q
#账号：88820212011
#密码：Abc123456！
#声音登录对应账户如上

for i in range(5):
    ##当前是声音登录方式
    if poco('点击按钮后，请按提示操作', text='点击按钮后，请按提示操作', timeout=1).exists():
        pass
    else:
        poco(text='换个方式登录').click()
        poco('声音登录', text='声音登录').click()
        poco('点击按钮后，请按提示操作', text='点击按钮后，请按提示操作', timeout=1).assert_exists()
    poco('登录', text='登录').click()
    poco('声音密码登录', text='声音密码登录').assert_exists()
    say(Audio('../../Design/Audios/你好英菲.wav'))
    if poco('账号', text='账号', timeout=10).exists():
        sleep(10)
        break
