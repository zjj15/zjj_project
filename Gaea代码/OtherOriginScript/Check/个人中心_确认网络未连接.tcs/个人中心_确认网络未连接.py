from autost.api import *

for i in range(3):
    if poco('登录', text='登录', timeout=1.5).exists():
        poco('登录', text='登录').click()
    elif poco('重新体检', text='重新体检', timeout=1.5).exists():
        poco('重新体检', text='重新体检').click()
    else:
        print('unknown situation')
    if exists(Template('../../Design/个人中心_tip_网络不可用.png'), timeout=3):
        sleep(3)
        break
else:
    error(__file__+' check error')
