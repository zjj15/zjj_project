from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'

'''
touch([430, 260],device=DEV1)
if poco('讯飞车机输入法').exists():
    poco('讯飞车机输入法').click()
'''


if poco(text='取消').exists():
    poco(text='取消').click()

if poco('讯飞车机输入法').exists():
    poco('讯飞车机输入法').click()

