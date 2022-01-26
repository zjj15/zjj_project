from autost.api import *

DEV1 = 'Gaea://127.0.0.1:5037/GFEDCBA0987654321'


temperature = poco(pos2 = [1120, 190]).get_attr('text')

if temperature[-1:] == '℃' and int(temperature[:-1]) in range(-50,50):
    pass
else:
    error('wrong temperature display')
