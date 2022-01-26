from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

poco('清除系统缓存', text='清除系统缓存', timeout=3).assert_exists()
poco('是', text='是', timeout=3).assert_exists()
poco('否', text='否', timeout=3).assert_exists()
poco('否', text='否', timeout=3).click()
