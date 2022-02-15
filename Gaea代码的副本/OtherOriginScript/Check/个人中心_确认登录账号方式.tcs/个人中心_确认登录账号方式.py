from autost.api import *

#1.扫描二维码登录
poco('推荐使用英菲智联APP扫码自动登录', text='推荐使用英菲智联APP扫码自动登录').assert_exists()

#2.输入账号名称和密码登录
if exists(Template('../../Design/个人中心_账号88820212011.png'), threshold=0.96, timeout=2):
   pass
else:
    poco(text='请输入登录账号').assert_exists()
poco('请输入登录密码', text='请输入登录密码').assert_exists()
#3.Vr登录
try:
    poco('换个方式登录', text='换个方式登录').click()
    poco('声音登录', text='声音登录').assert_exists()
    for _ in range(3):
        if poco('com.szlanyou.usercenter:id/view_cancel',pos2=[710, 251], timeout=1.5).exists():
            poco('com.szlanyou.usercenter:id/view_cancel',pos2=[710, 251]).click()
        if poco('登录', text='登录').exists():
            break
finally:
    for _ in range(2):
        if poco('com.szlanyou.usercenter:id/view_cancel',pos2=[710, 251], timeout=1.5).exists():
            poco('com.szlanyou.usercenter:id/view_cancel',pos2=[710, 251]).click()