from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

poco('清空观看历史', text='清空观看历史').assert_exists()
poco('是否清空全部观看历史？', text='是否清空全部观看历史？').assert_exists()
poco('是', text='是').assert_exists()
poco('否', text='否').assert_exists()

