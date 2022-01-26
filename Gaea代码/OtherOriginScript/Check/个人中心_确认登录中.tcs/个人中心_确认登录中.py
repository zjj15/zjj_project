from autost.api import *


poco('账号', text='账号').assert_exists()
poco('卡包', text='卡包').assert_exists()
poco('订单', text='订单').assert_exists()
poco('消息', text='消息').assert_exists()
