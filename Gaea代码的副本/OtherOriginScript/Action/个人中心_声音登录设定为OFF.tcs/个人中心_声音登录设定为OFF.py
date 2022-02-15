from autost.api import *

if poco('账号设置', text='账号设置', timeout=2).exists():
    pass
else:
    poco('账号', text='账号').click()
    poco('账号设置', text='账号设置', timeout=2).assert_exists()

for _ in range(5):
    touch_if(Template("../../Design/个人中心_声音登switch_on.png"), timeout=2)
    if poco('关闭声音登录', text='关闭声音登录', timeout=1.2).exists():
        poco('确定', text='确定').click()
        sleep(0.5)
    else:
        break