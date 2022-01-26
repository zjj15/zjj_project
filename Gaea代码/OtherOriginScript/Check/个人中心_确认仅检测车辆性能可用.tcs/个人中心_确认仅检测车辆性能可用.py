from autost.api import *

try:
    poco('账号', text='账号').assert_exists()
    poco('账号', text='账号').click()
    poco('游客模式下只能使用车辆检测功能，请您登录车联账号体验更多功能', text='游客模式下只能使用车辆检测功能，请您登录车联账号体验更多功能').assert_exists()
    poco('取消', text='取消').click()
finally:
    if poco('账号', text='账号', timeout=2).exists():
        poco('账号', text='账号').click()
        poco('立即登录', text='立即登录').click()
        sleep(5)
