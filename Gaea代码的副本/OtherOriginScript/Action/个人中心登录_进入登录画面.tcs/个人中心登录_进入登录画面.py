from autost.api import *

CANBUS_CH1 = 'CANBus1'
CANBUS_CH2 = 'CANBus2'
#车型：P42Q
#账号：88820212011
#密码：Abc123456！


do_segment(Segment('../个人中心登录_退出登录.tcs'))

sleep(15)

if poco('com.szlanyou.usercenter:id/iv_login_way_icon').exists():
    poco('com.szlanyou.usercenter:id/iv_login_way_icon').click()
    poco(text='换个方式登录').click()
    poco(text='密码登录').click()

poco(text='请输入登录密码').click()
poco('请输入登录密码', text='请输入登录密码').assert_exists()
