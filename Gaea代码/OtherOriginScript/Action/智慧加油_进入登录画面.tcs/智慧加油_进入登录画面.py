from autost.api import *

#车型：P42Q
#账号：88820212011
#密码：Abc123456！

if poco('跳过', text='跳过').exists():
    poco('跳过', text='跳过').click()
    
if poco(text='去登录').exists():
    poco(text='去登录').click()
if poco('com.szlanyou.usercenter:id/iv_login_way_icon').exists():
    poco(text='换个方式登录').click()
    poco(text='密码登录').click()

poco('请输入登录密码', text='请输入登录密码').click()


