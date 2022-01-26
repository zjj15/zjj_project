from autost.api import *

# 1,扫描二维码登录
poco('推荐使用英菲智联APP扫码自动登录', text='推荐使用英菲智联APP扫码自动登录').assert_exists()
#2.输入账号名称和密码登录
poco('登录', text='登录', resourceId='com.szlanyou.usercenter:id/btn_login').assert_exists()
