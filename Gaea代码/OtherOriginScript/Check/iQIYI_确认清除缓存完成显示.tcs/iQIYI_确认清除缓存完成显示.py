from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

poco('清除缓存成功', text='清除缓存成功', timeout=5).assert_exists()

sleep(1)
