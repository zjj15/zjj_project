from autost.api import *

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
#车型：P42Q
#账号：88802170666 
#密码：abc123!!
do_segment(Segment("../设定时间同步.tcs"))

if poco(text='appVersion: 1.3.9.0 daId: IP42QA2005280013').exists():
    if poco('88802170666', text='88802170666', className='android.widget.EditText').exists():
        poco(text='请输入登录密码').click()
        touch_if(Template("../../Design/Keyboard_lower_alpha.png"), timeout=5)
        touch(Template("../../Design/Keyboard_lower_a.png"), timeout=5)
        touch(Template("../../Design/Keyboard_lower_b.png"), timeout=5)
        touch(Template("../../Design/Keyboard_lower_c.png"), timeout=5)
        touch(Template("../../Design/Keyboard_num_button.png"), timeout=5)
        touch(Template("../../Design/Keyboard_num_1.png"), timeout=2)
        touch(Template("../../Design/Keyboard_num_2.png"), timeout=2)
        touch(Template("../../Design/Keyboard_num_3.png"), timeout=2)
        touch(Template("../../Design/Keyboard_符号_！.png"), timeout=2)
        touch(Template("../../Design/Keyboard_符号_！.png"), timeout=2)
        
        
    elif poco(text='请输入登录账号').exists():
        poco(text='请输入登录账号').click()
        #输入账号
        touch(Template("../../Design/纯数字键盘_8.png"), timeout=2)
        touch(Template("../../Design/纯数字键盘_8.png"), timeout=2)
        touch(Template("../../Design/纯数字键盘_8.png"), timeout=2)
        touch(Template("../../Design/纯数字键盘_0.png"), timeout=2)
        touch(Template("../../Design/纯数字键盘_2.png"), timeout=2)
        touch(Template("../../Design/纯数字键盘_1.png"), timeout=2)
        touch(Template("../../Design/纯数字键盘_7.png"), timeout=2)
        touch(Template("../../Design/纯数字键盘_6.png"), timeout=2)
        touch(Template("../../Design/纯数字键盘_6.png"), timeout=2)
        touch(Template("../../Design/纯数字键盘_6.png"), timeout=2)
        touch(Template("../../Design/纯数字键盘_确认.png"), timeout=5)
        
    touch(Template("../../Design/Keyboard_input_confirm.png"), timeout=5)
poco(text='登录').click()

for _ in range(3):
    if exists(Template("../../Design/个人中心_登录MSG.png"), timeout=10):
        break
    else:
        poco(text='登录').click()
assert_exists(Template("../../Design/个人中心_账号mark.png"), timeout=5)
sleep(5)
