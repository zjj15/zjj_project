from autost.api import *

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
#车型：P42Q
#账号：88820212011
#密码：Abc123456！
## 输入错误密码，登录失败

if not exists(Template('../../Design/个人中心_账号88820212011.png'), threshold=0.96, timeout=2):
    for i in range(3):
        if exists(Template('../../Design/个人中心_登录输入框删除btn.png'), threshold=0.96, timeout=2):
            touch(Template('../../Design/个人中心_登录输入框删除btn.png'), threshold=0.96, timeout=2)
        else:
            break

    poco(text='请输入登录账号').click()
    #输入账号
    touch(Template('../../Design/纯数字键盘_8.png'), timeout=2)
    touch(Template('../../Design/纯数字键盘_8.png'), timeout=2)
    touch(Template('../../Design/纯数字键盘_8.png'), timeout=2)
    touch(Template('../../Design/纯数字键盘_2.png'), timeout=2)
    touch(Template('../../Design/纯数字键盘_0.png'), timeout=2)
    touch(Template('../../Design/纯数字键盘_2.png'), timeout=2)
    touch(Template('../../Design/纯数字键盘_1.png'), timeout=2)
    touch(Template('../../Design/纯数字键盘_2.png'), timeout=2)
    touch(Template('../../Design/纯数字键盘_0.png'), timeout=2)
    touch(Template('../../Design/纯数字键盘_1.png'), timeout=2)
    touch(Template('../../Design/纯数字键盘_1.png'), timeout=2)

    touch(Template('../../Design/纯数字键盘_确认.png'), timeout=5)
#输入密码

poco(text='请输入登录密码').click()
touch_if(Template('../../Design/Keyboard_return_button.png'), timeout=2)
touch_if(Template('../../Design/Keyboard_upper_alpha.png'), timeout=5)
touch(Template('../../Design/Keyboard_upper_A.png'), timeout=5)
touch(Template('../../Design/Keyboard_lower_alpha.png'), timeout=5)
touch(Template('../../Design/Keyboard_lower_b.png'), timeout=5)
touch(Template('../../Design/Keyboard_lower_c.png'), timeout=5)
touch(Template('../../Design/Keyboard_num_button.png'), timeout=5)
touch(Template('../../Design/Keyboard_num_1.png'), timeout=2)
touch(Template('../../Design/Keyboard_num_2.png'), timeout=2)
touch(Template('../../Design/Keyboard_num_3.png'), timeout=2)
touch(Template('../../Design/Keyboard_num_4.png'), timeout=2)
touch(Template('../../Design/Keyboard_num_5.png'), timeout=2)
touch(Template('../../Design/Keyboard_num_6.png'), timeout=2)
#touch(Template('../../Design/Keyboard_符号_！.png'), timeout=2)

touch(Template('../../Design/Keyboard_input_confirm.png'), timeout=5)
poco(text='登录').click()
