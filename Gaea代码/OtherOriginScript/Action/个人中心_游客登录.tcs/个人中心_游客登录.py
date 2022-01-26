from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

poco(text='换个方式登录').click()
poco('游客登录', text='游客登录').click()
assert_exists(Template("../../Design/个人中心_账号mark.png"),device=DEV1)
sleep(8)