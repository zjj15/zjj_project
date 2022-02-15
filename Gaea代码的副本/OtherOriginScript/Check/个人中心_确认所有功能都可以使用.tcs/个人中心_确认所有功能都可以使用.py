from autost.api import *

poco('账号', text='账号').assert_exists()
poco('卡包', text='卡包').assert_exists()
poco('订单', text='订单').assert_exists()
poco('消息', text='消息').assert_exists()
try:
    poco('账号', text='账号').click()
    poco('账号设置', text='账号设置').assert_exists()
finally:
    if poco('取消', text='取消', timeout=2).exists():
        poco('取消', text='取消').click()
