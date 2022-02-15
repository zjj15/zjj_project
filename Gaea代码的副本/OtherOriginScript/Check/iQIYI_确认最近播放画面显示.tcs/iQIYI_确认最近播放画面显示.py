from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

poco('清空观看历史', text='清空观看历史', timeout=3).assert_not_exists()
poco('我的', text='我的').assert_exists()
poco('我的收藏', text='我的收藏').assert_exists()
poco('观看历史', text='观看历史').assert_exists()
poco('设置', text='设置').assert_exists()
