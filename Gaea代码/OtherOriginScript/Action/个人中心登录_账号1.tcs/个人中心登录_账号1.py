from autost.api import *

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
#车型：P42Q
#账号：88820212011
#密码：Abc123456！

touch_if(Template('../../Design/车联服务画面.png'))
if poco(text='2G季包').exists():
    poco('com.szlanyou.usercenter:id/iv_cancel').click()
    poco(text='车联服务').click()
touch_if(Template('../../Design/车联服务画面.png'))




if poco(text='账号').exists():
    pass
else:
    do_segment(Segment('../设定时间同步.tcs'))
    if poco('com.szlanyou.usercenter:id/iv_login_way_icon').exists():
        poco('com.szlanyou.usercenter:id/iv_login_way_icon').click()
        poco(text='换个方式登录').click()
        poco(text='密码登录').click()
    
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
    for _ in range(3):
        if poco(text='请输入登录密码', timeout=1.5).exists():
            break
        if poco('android.widget.ImageView', pos2=[1526, 441], timeout=1.5).exists():
            poco('android.widget.ImageView', pos2=[1526, 441]).click()
        if poco('android.widget.ImageView', pos2=[1526, 238], timeout=1.5).exists():
            poco('android.widget.ImageView', pos2=[1526, 238]).click()

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

    touch(Template('../../Design/Keyboard_input_confirm.png'), timeout=5)
    poco(text='登录').click()
    for _ in range(3):
        if exists(Template('../../Design/个人中心_登录MSG.png'), timeout=10):
            break
        else:
            poco(text='登录').click()
    sleep(10)
    if poco(text='注册FaceID').exists():
        poco(text='注册FaceID').click()
        poco(text='下次再说').click()
    
    
    assert_exists(Template('../../Design/个人中心_账号mark.png'), timeout=5)
    sleep(5)
