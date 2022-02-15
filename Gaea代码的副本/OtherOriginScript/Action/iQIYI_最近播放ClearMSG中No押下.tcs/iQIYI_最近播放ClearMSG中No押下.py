from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

if poco('是否清空全部观看历史？', text='是否清空全部观看历史？', timeout=3).exists():
    poco('否', text='否').click()
