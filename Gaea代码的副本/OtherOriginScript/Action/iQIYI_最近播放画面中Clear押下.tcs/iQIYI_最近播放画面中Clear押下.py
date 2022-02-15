from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

if poco('清空', text='清空', timeout=1.5).exists():
    poco('清空', text='清空').click()