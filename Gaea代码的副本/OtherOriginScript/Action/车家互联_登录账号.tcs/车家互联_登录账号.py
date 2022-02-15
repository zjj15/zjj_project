from autost.api import *

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
#车型：P42Q
#账号：88820212011
if poco(text='请输入手机号码').exists():
    poco(text='请输入手机号码').click()

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
if poco(text='请输入登录密码').exists():
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
    touch(Template('../../Design/Keyboard_符号_！.png'), timeout=2)
